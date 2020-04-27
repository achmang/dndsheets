from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=18)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])

class SignupForm(FlaskForm):
    email = StringField('Email Address', validators=[InputRequired(), Email(message='Invalid Email')])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=18)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])

class CreateChar(FlaskForm):
    char_name = StringField('Name', validators=[InputRequired(), Length(min=2, max=60)])
    race = StringField('Race', validators=[InputRequired(), Length(min=2, max=60)])
    char_class = StringField('Class', validators=[InputRequired(), Length(min=2, max=60)])