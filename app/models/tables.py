from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from time import gmtime
from flask_sqlalchemy import SQLAlchemy


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String,unique=True)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def generate_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)

    def __init__(self,username,name,email):
        self.username = username
        self.name = name
        self.email = email
    def __repr__(self):
        return "<User %r>" % self.username

class Post(db.Model):
        __tablename__ = "posts"

        id = db.Column(db.Integer,primary_key=True)
        content = db.Column(db.Text)
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        minute = db.Column(db.Integer)
        second = db.Column(db.Integer)

        user = db.relationship('User', foreign_keys = user_id)

        def __init__(self,content,user_id):
            self.content = content
            self.user_id = user_id
            self.minute = gmtime()[4]
            self.second = gmtime()[5]
        def __repr__(self):
            return "<Post %r>" %self.id

class Follow(db.Model):
    __tablename__ = "follow"

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys = user_id)
    follower = db.relationship('User', foreign_keys =follower_id)

    def __init__(self,user_id,follower_id):
        self.user_id = user_id
        self.follower_id = follower_id

    def __repr__(self):
        return "<Follow %r>" % self.id
