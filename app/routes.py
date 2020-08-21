from flask import render_template, url_for, flash, redirect, request, abort
from app.models import User, Post
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
# ! here inport bcrypt not Bcrypt
from app import application, db, bcrypt
from flask_login import login_user, current_user, logout_user,login_required
from .main import run_result

# call crawler
@application.route('/e/e')
def call_crawler():
    print('be called')
    return run_result()
    
@application.route('/')
@application.route('/home')
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

# method=['GET', 'POST'] allows get and post in this page
@application.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    # if submitted content is validated, flash and return to home page
    if form.validate_on_submit():
        # hash password from form
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # create a user and save it into DB
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash(f'Account created for {form.username.data}!', category='success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@application.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # if user exists and the password is correct
        # user.password from DB, and second parameter from input
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # don't rearch this function
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful', category='danger')
    return render_template('login.html', title='Login', form=form)

@application.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@application.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    update_form = UpdateAccountForm()
    if update_form.validate_on_submit():
        current_user.username = update_form.username.data
        current_user.email = update_form.email.data
        db.session.commit()
        flash('Your account has been updated', category='success')
        # return here to avoid something
        return redirect(url_for('account'))
    elif request.method == "GET":
        update_form.username.data = current_user.username
        update_form.email.data = current_user.email
    image_file = url_for('static', filename=current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=update_form)

@application.route("/post/new", methods=['GET', 'POST'])
@login_required
def post_new():
    post_form = PostForm()
    if post_form.validate_on_submit():
        post = Post(title=post_form.title.data, content=post_form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()

        flash('Your post has been created', category='success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', form=post_form, legend='New Post')


@application.route("/post/<int:post_id>")
def post(post_id):
    # get page or return 404 no found
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@application.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        # Request Forbidden
        abort(403)

    update_form = PostForm()
    if update_form.validate_on_submit():
        post.title = update_form.title.data
        post.content = update_form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        update_form.title.data = post.title
        update_form.content.data = post.content
        
    return render_template('create_post.html', title='Update Post',
                           form=update_form, legend='Update Post')


@application.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))