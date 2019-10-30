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

@main.route('/add/category', methods=['GET','POST'])
@login_required
def new_category():
    '''
    View new group route function that returns a page with a form to create a category
    '''
    form = CategoryForm()

    if form.validate_on_submit():
        name = form.name.data
        new_category = ArticleCategory(name=name)
        new_category.save_category()

        return redirect(url_for('.index'))

    title = 'New category'
    return render_template('new_category.html', category_form = form,title=title) 

@main.route('/view-articles/<int:id>', methods=['GET', 'POST'])
@login_required
def view_articles(id):
    '''
    Function the returns a single article for comment to be added
    '''
    print(id)
    articles = Article.query.get(id)


    if articles is None:
        abort(404)
    #
    comment = Comments.get_comments(id)
    up_likes = UpVote.get_votes(id)
    down_likes = DownVote.get_downvotes(id)
    return render_template('view-article.html', articles=articles, comment=comment, category_id=id,likes=up_likes,dislike=down_likes)             

@main.route('/write_comment/<int:id>', methods=['GET', 'POST'])
@login_required
def post_comment(id):
    ''' function to post comments '''
    form = CommentForm()
    title = 'post comment'
    articles = Blog.query.filter_by(id=id).first()

    if articles is None:
         abort(404)

    if form.validate_on_submit():
        opinion = form.opinion.data
        new_comment = Comments(opinion=opinion, articles_id=articles.id)
        new_comment.save_comment()
        return redirect(url_for('.view_artilces', id=artilces.id))

    return render_template('post_comment.html', comment_form=form, title=title)
