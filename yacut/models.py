from datetime import datetime

from flask import url_for

from settings import USER_LINK_LENGHT
from yacut import db


class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(), index=True, nullable=False)
    short = db.Column(db.String(USER_LINK_LENGHT), index=True, unique=True,
                      nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for('redirect_view', short=self.short,
                               _external=True)
        )
