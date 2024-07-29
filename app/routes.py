from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from app.utils import generate_sentiment_pie_chart, generate_sentiment_table, clear_database, fetch_posts

bp = Blueprint('routes', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/visualization', methods=['GET'])
def visualization():
    pie_chart_html = generate_sentiment_pie_chart()
    sentiment_table_html = generate_sentiment_table()
    return f"""
    <html>
        <head>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            </head>
            <body>
                <h1>Reddit Sentiment Analysis</h1>
                <div>{pie_chart_html}</div>
                <h2>Sentiment Scores Table</h2>
                <div>{sentiment_table_html}</div>
            </body>
        </html>
        """


@bp.route('/fetch_posts', methods=['GET'])
def fetch_subreddit_posts():
    subreddit = request.args.get('subreddit')
    if subreddit:
        clear_database()

        fetch_posts(subreddit)

        return redirect(url_for('routes.visualization'))
    return redirect(url_for('routes.index'))
