from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

'''
class RegistrationForm(FlaskForm):
  # validators always be an array (I think)
  # Limit definition:
  # 1. Datarequired() = must have data in the form
  # 2. class Length defines the lengh of username
  username = StringField('Username', 
                          validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField('Email', 
                      validators=[DataRequired(), Email()])                    
  password = PasswordField('Password', validators=[DataRequired()]) 
  confirm_password = PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password')])      
  submit = SubmitField('Sign up')

  # custom validation
  def validate_username(self, username):

    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError('choose new username plz')
    
  def validate_email(self, email):

    user = User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError('choose new email plz')


class LoginForm(FlaskForm):
  email = StringField('Email', 
                      validators=[DataRequired(), Email()])                    
  password = PasswordField('Password', validators=[DataRequired()]) 
  # for cookie
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')
'''
'''
Form(input) to update account
'''
'''
class UpdateAccountForm(FlaskForm):
  # validators always be an array (I think)
  # Limit definition:
  # 1. Datarequired() = must have data in the form
  # 2. class Length defines the lengh of username
  username = StringField('Username', 
                          validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField('Email', 
                      validators=[DataRequired(), Email()])                    
    
  submit = SubmitField('Update')

  # custom validation
  def validate_username(self, username):
    if username.data != current_user.username:
      user = User.query.filter_by(username=username.data).first()
      if user:
        raise ValidationError('choose new username plz')
    
  def validate_email(self, email):
    if email.data != current_user.email:
      user = User.query.filter_by(email=email.data).first()
      if user:
         raise ValidationError('choose new email plz')
'''
class PostForm(FlaskForm):
  '''The form to post into database'''
  title = StringField('Title', validators=[DataRequired()])
  content = TextAreaField('Content', validators=[DataRequired()])
  submit = SubmitField('Post')



