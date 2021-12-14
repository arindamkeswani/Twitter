# from __init__ import db, login_manager
from modules import db, login_manager
from sqlalchemy.orm import backref #Creates a pseudo column in the child table
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id) 

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    profile_image = db.Column(db.String(100), nullable=False, default='default.jpg')
    background_image = db.Column(db.String(100), nullable=False, default='default_bg.jpg')
    bio= db.Column(db.String(280))
    date= db.Column(db.String(20))
    bday= db.Column(db.String(20))

    posts = db.relationship('Post', backref="author", lazy=True)
    retweeted = db.relationship('Retweet', backref="retweeter", lazy=True)
    bookmarked = db.relationship('Bookmark', backref="saved_by", lazy=True)


class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    tweet = db.Column(db.String(500),nullable=False)
    stamp = db.Column(db.String(20),nullable=False)
    post_img = db.Column(db.String(20))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    likes = db.Column(db.Integer, nullable=False, default=0)
    likers = db.relationship('Likes',backref="liked_by", lazy=True)

    commenters = db.relationship('Comments',backref="commented_by", lazy=True)

    retweet = db.relationship('Retweet', backref="ori_post", lazy=True)
    timeline = db.relationship('Timeline', backref="from_post", lazy=True)
    bookmark = db.relationship('Bookmark', backref="saved_post", lazy=True)

    

class Retweet(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    tweet_id = db.Column(db.Integer,db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    retweet_stamp = db.Column(db.String(20),nullable=False)
    retweet_text = db.Column(db.String(500),nullable=False)

    likes = db.Column(db.Integer, nullable=False, default=0)
    likers = db.relationship('Likes',backref='rt_liked_by',lazy=True)
    commenters = db.relationship('Comments',backref="rt_commented_by", lazy=True)
    timeline = db.relationship('Timeline', backref="from_retweet", lazy=True)

class Timeline(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    post_id = db.Column(db.Integer,db.ForeignKey('post.id'),default=None)
    retweet_id = db.Column(db.Integer,db.ForeignKey('retweet.id'),default=None)

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'),default=None)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),default=None)

class Likes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer,db.ForeignKey('post.id'), default=None)
    retweet_id=db.Column(db.Integer,db.ForeignKey('retweet.id'),default=None)
    liker=db.Column(db.String(20), default=None)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),default=None)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer,db.ForeignKey('post.id'),default=None)
    retweet_id=db.Column(db.Integer,db.ForeignKey('retweet.id'),default=None)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),default=None)
    comment = db.Column(db.String(240))
    commenter = db.Column(db.String(20), default=None)
    comment_stamp = db.Column(db.String(20),nullable=False)


db.create_all()

