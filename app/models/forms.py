from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,TextAreaField
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):
	username = StringField("username", validators=[DataRequired()])
	password = PasswordField("password", validators=[DataRequired()])
	name = StringField("name", validators=[DataRequired()])
	email = StringField("email", validators=[Email()])

class LoginForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    remember_me = BooleanField('remember_me')

class TwitForm(FlaskForm):
	content = TextAreaField('content',validators=[DataRequired()])