from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import *
from ..models import *
from flask_login import login_required, current_user
from ..import db,photos
import markdown2
from ..email import mail_message
from ..requests import get_quotes

@main.route('/')
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    quotes = get_quotes()
    return render_template('index.html', quotes=quotes, posts=posts)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)  