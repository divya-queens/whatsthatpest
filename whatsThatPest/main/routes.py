from flask import render_template, request, Blueprint, redirect, url_for
from flask_login import current_user, login_required
from whatsThatPest import db
from whatsThatPest.models import Post
from whatsThatPest.main.forms import BugRecognitionForm
from whatsThatPest.main.utils import save_picture, bug_recognition
from whatsThatPest.models import Bug
from whatsThatPest.Bug import bug_info

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

@main.route("/home")
@login_required
def home():
    form = BugRecognitionForm()
    posts = Post.query.order_by(Post.date_posted.desc())
    post_count = posts.count()
    
    return render_template('home.html', form=form, posts=posts, post_count=post_count)

@main.route("/recognize", methods=['POST'])
@login_required
def recognize():
    form = BugRecognitionForm()

    if form.validate_on_submit():
        if form.picture.data:
            bug_file = save_picture(form.picture.data)
            bug_name = bug_recognition(bug_file)
        
            bug = Bug(name=bug_name, bug_image=bug_file, author=current_user)
            db.session.add(bug)
            db.session.commit()
            bug_data = bug_info[bug_name]
            image_source = bug_name + ".jpg"

    return render_template('bug_info.html', image_source=image_source, bug_name=bug_name, bug_damage=bug_data.get_damage(), bug_description = bug_data.get_description(), bug_pesticides = bug_data.get_pesticide())
 

