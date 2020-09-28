from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# EB looks for an 'application' callable by default.
app = Flask(__name__)
#  for cross-site request forgery agianst attack
app.config['SECRET_KEY'] = '4e57a23642728784e88ef62c418e1318'
# set database uri
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# to initialize
db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager = LoginManager(application)

#login is function name in routes.py
login_manager.login_view = 'login'

login_manager.login_message_category = 'info'

# this must be unter applcation to avoid circular import
from app import routes