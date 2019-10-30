from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from .forms import ReviewForm,CategoryForm,CommentForm,BlogForm
from ..models import ArticleCategory,Article,Comments,UpVote,DownVote
# from ..models import Review
# Review = review.Review
#display categories on the landing page
from ..request import get_quote

@main.route('/')
def index():
    """ View root page function that returns index page """

    category = ArticleCategory.get_categories()
    quote = get_quote()

    title = 'Home- Welcome'
    return render_template('index.html', title = title, categories=category, quote=quote)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)  

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))    