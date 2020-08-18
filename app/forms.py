from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

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

class LoginForm(FlaskForm):
  email = StringField('Email', 
                      validators=[DataRequired(), Email()])                    
  password = PasswordField('Password', validators=[DataRequired()]) 
  # for cookie
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')