from flask import render_template, request, Blueprint, redirect, url_for
from flask_login import current_user, login_required
from whatsThatPest import db
from whatsThatPest.models import Post
from whatsThatPest.main.forms import BugRecognitionForm
from whatsThatPest.main.utils import save_picture, bug_recognition
from whatsThatPest.models import Bug

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/index")
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    return render_template('index.html')

@main.route("/about")
def about():
    return render_template('about.html')

@main.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    form = BugRecognitionForm()

    if form.validate_on_submit():
        if form.picture.data:
            bug_file = save_picture(form.picture.data)
            bug_name = bug_recognition(bug_file)
        
            bug = Bug(name=bug_name, bug_image=bug_file, author=current_user)
            db.session.add(bug)
            db.session.commit()
            return '<h1>Lady Bug</h1>'

    elif request.method == 'GET':
        posts = Post.query.order_by(Post.date_posted.desc())
        return render_template('home.html', form=form, posts=posts)


