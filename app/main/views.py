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


@main.route('/category/new-article/<int:id>', methods=['GET', 'POST'])
@login_required
def new_article(id):
    ''' Function to check Blogs form and fetch data from the fields '''
    form = ArticleForm()
    category = ArticleCategory.query.filter_by(id=id).first()

    if category is None:
        abort(404)

    if form.validate_on_submit():
        content= form.content.data
        new_article= Article(content=content,category_id= category.id)
        new_article.save_blog()
        return redirect(url_for('.category', id=category.id))

 

    return render_template('new_article.html', article_form=form, category=category)       