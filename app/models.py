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
    pass_secure = db.Column( db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    categories = db.relationship("Article", backref="user1", lazy="dynamic")
    comment = db.relationship("Comments", backref="user2", lazy="dynamic")
    upvotes = db.relationship("UpVote", backref="article2", lazy="dynamic")
    downvotes = db.relationship("DownVote", backref="article2", lazy="dynamic")

   
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f' {self.username}'
        
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

class Article(db.Model):
    """ List of articles in each category """

    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment = db.relationship("Comments", backref="article1", lazy="dynamic")

    def save_article(self):
        ''' Save the blocks '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_(cls):
        Article.all_articles.clear()

    # display articles

    def get_articles(id):
        articles = Article.query.filter_by(category_id=id).all()
        return articles             


class Comments(db.Model):
    '''User comment model for each article '''

    __tablename__ = 'comments'

    # add columns
    id = db.Column(db. Integer, primary_key=True)
    opinion = db.Column(db.String(255))
    time_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    articles_id = db.Column(db.Integer, db.ForeignKey("articles.id"))

    def save_comment(self):
        '''
        Save the Comments/comments per article
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comment = Comments.query.order_by(
        Comments.time_posted.desc()).filter_by(articles_id=id).all()
        return comment

class UpVote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key=True)
    id_user = db.Column(db.Integer,db.ForeignKey('users.id'))
    article_id = db.Column(db.Integer)

    def save_vote(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_votes(cls,id):
        upvote = UpVote.query.filter_by(article_id=id).all()
        return upvote
    
    def __repr__(self):
        return f'{self.id_user}:{self.article_id}'       

class DownVote(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key=True)
    id_user = db.Column(db.Integer,db.ForeignKey('users.id'))
    article_id = db.Column(db.Integer)

    def save_vote(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_downvotes(cls,id):
        downvote = DownVote.query.filter_by(article_id=id).all()
        return downvote
        
    def __repr__(self):
        return f'{self.id_user}:{self.article_id}'

class Quotes():
    """
    class to display random quotes
    """      

    def __init__(self,author,quote,permalink):
        self.author = author
        self.quote = quote
        self.permalink = permalink   
        
               