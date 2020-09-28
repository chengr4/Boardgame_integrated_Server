from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# EB looks for an 'application' callable by default.
application = Flask(__name__)
#  for cross-site request forgery agianst attack
application.config['SECRET_KEY'] = '4e57a23642728784e88ef62c418e1318'

# set database uri (local)
#application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# set database uri (online)
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://drvdyfommfmtgt:'+
'a18dd8832f85b2002fd471d3f032875345fff0eb45e69cfbae88cc47e99f2c60@ec2-3-224-97-209.compute-1.amazonaws.com:5432/dd91muj73h8bjd'

# to initialize
db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager = LoginManager(application)

#login is function name in routes.py
login_manager.login_view = 'login'

login_manager.login_message_category = 'info'

# this must be unter applcation to avoid circular import
from app import routes