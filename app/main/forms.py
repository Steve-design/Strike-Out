
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

<<<<<<< HEAD
class ReviewForm(FlaskForm):
    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Article review', validators=[Required()])
    submit = StringField('Submit')
=======
<<<<<<< HEAD

=======
>>>>>>> master
>>>>>>> Development
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
<<<<<<< HEAD
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
=======
    comment = TextAreaField('Leave your comment...',validators = [Required()])
<<<<<<< HEAD
    submit = SubmitField('Submit')  
=======
    submit = SubmitField('Submit') 
>>>>>>> master

class AddPost(FlaskForm):
    title = TextAreaField('Title.')
    subtitle = TextAreaField('Subtitle.')
    content = TextAreaField('Content')
<<<<<<< HEAD
    submit = SubmitField('Submit')         
=======
    submit = SubmitField('Submit')          
>>>>>>> master
>>>>>>> Development
