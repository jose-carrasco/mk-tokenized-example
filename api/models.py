import time
import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(40),)

    def __str__(self):
        return "User(id='%s')" % self.id


    def get_user_id(self):
        return self.id

    def check_password(self, password):
        return self.password == password


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surename = db.Column(db.String(100))
    token = db.Column(db.String(50), unique=True)
    mobile_number = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)

    def __str__(self):
        return self.username

    def get_user_id(self):
        return self.id
