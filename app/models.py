from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin

''' For database'''

'''
# for reloading the user from the user ID stored in session
# ????? not sure what is for
@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))
'''

# UserMixin provides some methods, i am just too lazy to check
class User(db.Model, UserMixin):
    '''Interface for user table'''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # make relationship with post
    # backref is similar to adding another column to the Post Model
    # with backref we can simple use the attribute to get the user who creates the post 
    posts = db.relationship('Post', backref='author', lazy=True)

    # How the object is printed out
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    '''Interface for post table'''
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"