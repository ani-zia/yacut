from datetime import datetime

from yacut import db

from settings import USER_LINK_LENGHT


class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(), index=True, nullable=False)
    short = db.Column(db.String(USER_LINK_LENGHT), index=True, unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
