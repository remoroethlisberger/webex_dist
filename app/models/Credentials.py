from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from db import db


class Credentials(db.Model):
    """Model for credentials."""
    __tablename__ = 'credentials'

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String, nullable=False, unique=False)
    email = db.Column(db.String(40), unique=False, nullable=False)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    valid = db.Column(db.Boolean)

    def __init__(self, token, email):
        self.token = token
        self.email = email
        self.created_on = datetime.now()
        self.valid = True

    def __repr__(self):
        return '<Credentials {}>'.format(self.token)
