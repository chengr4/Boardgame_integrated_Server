from flask import render_template, url_for, flash, redirect
from app.models import User, Post
from app.forms import RegistrationForm, LoginForm
from app import application

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

@application.route('/')
def root():
    return "Yo!!"


# call crawler
@application.route('/e/e')
def call_crawler():
    print('be called')
    return run_result()
    
@application.route('/home')
def home():
    return render_template('home.html', posts=posts)

# method=['GET', 'POST'] allows get and post in this page
@application.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # if submitted content is validated, flash and return to home page
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', category='success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@application.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)