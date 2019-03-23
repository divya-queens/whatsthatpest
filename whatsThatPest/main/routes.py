from flask import render_template, request, Blueprint, redirect, url_for
from flask_login import current_user
from whatsThatPest.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/index")
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    return render_template('index.html')

@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

