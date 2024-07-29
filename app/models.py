from app import db


class Post(db.Model):
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    sentiment_pos = db.Column(db.Float, nullable=False)
    sentiment_neg = db.Column(db.Float, nullable=False)
    sentiment_neu = db.Column(db.Float, nullable=False)
    sentiment_compound = db.Column(db.Float, nullable=False)
    url = db.Column(db.String(200))
