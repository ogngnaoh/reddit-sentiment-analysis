import praw
from flask import current_app
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import plotly.graph_objects as go
import pandas as pd
from app.models import Post
from app import db

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()


def get_reddit_instance():
    reddit = praw.Reddit(
        client_id=current_app.config['REDDIT_CLIENT_ID'],
        client_secret=current_app.config['REDDIT_CLIENT_SECRET'],
        user_agent=current_app.config['REDDIT_USER_AGENT']
    )
    return reddit


def fetch_posts(subreddit, limit=10):
    reddit = get_reddit_instance()
    posts = reddit.subreddit(subreddit).hot(limit=limit)
    analyzed_posts = []
    for post in posts:
        sentiment = sia.polarity_scores(post.title + ' ' + post.selftext)
        comments = post.comments.list()
        comment_count = 0
        for comment in comments:
            if isinstance(comment, praw.models.Comment):
                comment_sentiment = sia.polarity_scores(comment.body)
                sentiment['pos'] += comment_sentiment['pos']
                sentiment['neg'] += comment_sentiment['neg']
                sentiment['neu'] += comment_sentiment['neu']
                sentiment['compound'] += comment_sentiment['compound']
                comment_count += 1

        if comment_count > 0:
            sentiment['pos'] /= comment_count + 1
            sentiment['neg'] /= comment_count + 1
            sentiment['neu'] /= comment_count + 1
            sentiment['compound'] /= comment_count + 1

        new_post = Post(
            id=post.id,
            title=post.title,
            body=post.selftext,
            sentiment_pos=sentiment['pos'],
            sentiment_neg=sentiment['neg'],
            sentiment_neu=sentiment['neu'],
            sentiment_compound=sentiment['compound'],
            url=post.url,
        )
        db.session.add(new_post)
        db.session.commit()
        analyzed_posts.append(new_post)
    return analyzed_posts


def clear_database():
    try:
        num_rows_deleted = db.session.query(Post).delete()
        db.session.commit()
        return num_rows_deleted
    except Exception as e:
        db.session.rollback()
        print(f"Error clearing database: {e}")
        return 0


def generate_sentiment_pie_chart():
    posts = Post.query.all()

    total_posts = len(posts)

    total_positive = sum(post.sentiment_pos for post in posts)
    total_negative = sum(post.sentiment_neg for post in posts)
    total_neutral = sum(post.sentiment_neu for post in posts)

    avg_positive = total_positive / total_posts if total_posts else 0
    avg_negative = total_negative / total_posts if total_posts else 0
    avg_neutral = total_neutral / total_posts if total_posts else 0

    fig = go.Figure(data=[go.Pie(labels=['Positive', 'Negative', 'Neutral'],
                                 values=[avg_positive, avg_negative, avg_neutral],
                                 hole=.3)])

    fig.update_layout(
        title_text='Average Sentiment Distribution',
    )

    return fig.to_html(full_html=False)


def generate_sentiment_table():
    posts = Post.query.all()

    data = {
        'Title': [post.title for post in posts],
        'Positive': [post.sentiment_pos for post in posts],
        'Negative': [post.sentiment_neg for post in posts],
        'Neutral': [post.sentiment_neu for post in posts],
        'Compound': [post.sentiment_compound for post in posts]
    }

    df = pd.DataFrame(data)
    return df.to_html(classes='table table-striped', index=False)
