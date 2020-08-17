from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
from main import run_result


# EB looks for an 'application' callable by default.
application = Flask(__name__)

#  for cross site re quest forgery agianst attack
application.config['SECRET_KEY'] = '4e57a23642728784e88ef62c418e1318'

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
@application.route('/register', method=['GET', 'POST'])
def register():
    form =RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@application.route('/login')
def login():
    form =LoginForm()
    return render_template('login.html', title='Login', form=form)


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()



