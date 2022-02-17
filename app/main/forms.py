from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired

class CommentForm(FlaskForm):

    comment = StringField('Comment', validators=[InputRequired()])
    submit = SubmitField('Submit')

class QuoteForm(FlaskForm):
    author = StringField('Author',)
    quote = TextAreaField('Post your quote', validators=[InputRequired()])
    submit = SubmitField('Post Quote')

class QuoteCommentForm(FlaskForm):

    comment = StringField('Comment', validators=[InputRequired()])
    submit = SubmitField('Submit')