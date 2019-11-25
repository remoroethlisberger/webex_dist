from db import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(500))

    def __init__(self, username, password):
        self.username = username
        self.password = password
