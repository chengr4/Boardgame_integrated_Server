from flask import render_template, url_for, flash, redirect
from app.models import User, Post
from app.forms import RegistrationForm, LoginForm
# ! here inport bcrypt not Bcrypt
from app import application, db, bcrypt
from flask_login import login_user, current_user, logout_user,login_required
from .main import run_result

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]





# call crawler
@application.route('/e/e')
def call_crawler():
    print('be called')
    return run_result()
    
@application.route('/')
@application.route('/home')
def home():
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

@application.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')