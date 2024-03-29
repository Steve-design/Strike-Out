from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from .forms import ReviewForm,CategoryForm,CommentForm,ArticleForm
from ..models import ArticleCategory,Article,Comments,UpVote,DownVote
# from ..models import Review
# Review = review.Review
#display categories on the landing page
from ..requests import get_quote

@main.route('/')
def index():
    """ View root page function that returns index page """

    category = ArticleCategory.get_categories()
    quote = get_quote()

    title = 'Home- Welcome'
    return render_template('index.html', title = title, categories=category, quote=quote)




@main.route('/category/new_article/<int:id>', methods=['GET', 'POST'])
@login_required
def new_article(id):
    ''' Function to check Articles form and fetch data from the fields '''
    form = ArticleForm()
    category = ArticleCategory.query.filter_by(id=id).first()

    if category is None:
        abort(404)

    if form.validate_on_submit():
        content= form.content.data
        new_article= Article(content=content,category_id= category.id)
        new_article.save_article()
        return redirect(url_for('.category', id=category.id))

 

    return render_template('new_article.html', article_form=form, category=category)

@main.route('/categories/<int:id>')
def category(id):
    category = ArticleCategory.query.get(id)
    if category is None:
        abort(404)

    articles=Article.get_articles(id)
    return render_template('category.html', articles=articles, category=category)

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
    return render_template('view_article.html', articles=articles, comment=comment, category_id=id,likes=up_likes,dislike=down_likes)


@main.route('/write_comment/<int:id>', methods=['GET', 'POST'])
@login_required
def post_comment(id):
    ''' function to post comments '''
    form = CommentForm()
    title = 'post comment'
    articles = Article.query.filter_by(id=id).first()

    if articles is None:
         abort(404)

    if form.validate_on_submit():
        opinion = form.opinion.data
        new_comment = Comments(opinion=opinion, articles_id=articles.id)
        new_comment.save_comment()
        return redirect(url_for('.view_articles', id=articles.id))

    return render_template('post_comment.html', comment_form=form, title=title)

@main.route('/home/like/<int:id>', methods = ['GET','POST'])
@login_required
def like(id):
    get_article = UpVote.get_votes(id)
    valid_string = f'{current_user.id}:{id}'

    for get_article in get_article:
        to_str = f'{get_article}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.view_articles',id=id))
        else:
            continue

    like_article = UpVote( article_id=id)
    like_article.save_vote()

    return redirect(url_for('main.view_articles',id=id))

@main.route('/home/dislike/<int:id>', methods = ['GET','POST'])
@login_required
def dislike(id):
    get_article = DownVote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'

    for get_article in get_article:
        to_str = f'{get_article}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.view_articles',id=id))
        else:
            continue

    dislike_article = DownVote( article_id=id)
    dislike_article.save_vote()

    return redirect(url_for('main.view_articles',id=id))    