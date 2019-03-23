from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField


class BugRecognitionForm(FlaskForm):
    picture = FileField('Upload bug picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('upload')