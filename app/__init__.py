from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.main import run_result


# EB looks for an 'application' callable by default.
application = Flask(__name__)
#  for cross-site request forgery agianst attack
application.config['SECRET_KEY'] = '4e57a23642728784e88ef62c418e1318'
# set database uri
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(application)

# this must be unter applcation to avoid circular import
from app import routes