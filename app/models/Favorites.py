from db import db


class Favorites(db.Model):
    """Model for favorites."""
    __tablename__ = 'favorites'

    id = db.Column(db.Integer, primary_key=True)
    roomid = db.Column(db.String, nullable=False, unique=False)

    def __init__(self, roomid):
        self.roomid = roomid

    def __repr__(self):
        return '<Favorites {}>'.format(self.token)
