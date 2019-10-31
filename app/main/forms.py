
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):
    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Article review', validators=[Required()])
    submit = StringField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
class CategoryForm(FlaskForm):
    '''
    Class to create a wtf form for creating an article
    '''
    name =  StringField('Category Name', validators=[Required()])
    submit = SubmitField('Create')
class CommentForm(FlaskForm):
    '''
    Class to create a wtf form for creating an article
    '''
    opinion = TextAreaField('WRITE COMMENT')
    submit = SubmitField('SUBMIT')
class ArticleForm(FlaskForm):
    '''
    Class to create a wtf form for creating a pitch
    '''
    title = TextAreaField('Title.')
    content = TextAreaField('YOUR ARTICLE')
    submit = SubmitField('CREATE')
