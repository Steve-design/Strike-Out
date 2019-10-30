from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from sqlalchemy.sql import func

@login_manager.user_loader
def load_user(user_id):
    '''
    @login_manager.user_loader Passes in a user_id to this function
    Function queries the database and gets a user's id as a response
    '''
    return User.query.get(int(user_id))

class Quote:
    '''
    Quote class to define Quote Objects
    '''

    def __init__(self, author, quote):
        self.author = author
        self.quote = quote


class User(UserMixin, db.Model):
    """ class modelling the users """

    __tablename__ = 'users'

    # create the columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    categories = db.relationship("Article", backref="user1", lazy="dynamic")
    comment = db.relationship("Comments", backref="user2", lazy="dynamic")
    upvotes = db.relationship("UpVote", backref="article2", lazy="dynamic")
    downvotes = db.relationship("DownVote", backref="article2", lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You can not read the password Attribute')

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class ArticleCategory(db.Model):

    __tablename__ = 'categories'

    # table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    # save articles
    def save_category(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        categories = ArticleCategory.query.all()
        return categories        