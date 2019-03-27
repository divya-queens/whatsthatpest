from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()], render_kw={"rows": 10})
    picture = FileField('Add a Picture to your post', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Post')
