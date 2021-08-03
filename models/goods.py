from flask_login import UserMixin
from app import db


class Goods(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(1000))
    price = db.Column(db.Integer(), nullable=False)

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
