from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired

class CommentForm(FlaskForm):

    comment = StringField('Comment', validators=[InputRequired()])
    submit = SubmitField('Submit')