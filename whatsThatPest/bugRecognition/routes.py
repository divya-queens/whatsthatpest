from flask import render_template, Blueprint
from flask_login import login_required
from whatsThatPest.bugRecognition.forms import (BugRecognitionForm)
from whatsThatPest.bugRecognition.utils import save_picture

bugRecognition = Blueprint('bugRecognition', __name__)


@bugRecognition.route("/about", methods=['GET', 'POST'])
@login_required
def about():
    form = BugRecognitionForm()
    if form.validate_on_submit():
        if form.picture.data:
            bug_file = save_picture(form.picture.data)

        #db.session.commit()

    return render_template('about.html', title='Bug', form=form)
