from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

<<<<<<< HEAD

=======
>>>>>>> master
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
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
