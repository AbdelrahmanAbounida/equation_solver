from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired,InputRequired,Email,EqualTo, Length,ValidationError
from .models import User

def UniqueValidator(form, field):
    if User.query.filter_by(email = field.data).first():
        raise ValidationError("A user with the same email already exist")


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(),Email(message='PLease enter a valid email address')])
    password = PasswordField('Password', [InputRequired(),Length(min=4,message="Password min length is 4")])
    submit = SubmitField(label="Login")



class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(),Email(message='Please enter a valid email address'),UniqueValidator])
    password  = PasswordField('New Password',[InputRequired(),Length(min=4,message="Password min length is 4")])
    confirm = PasswordField('Repeat Password', [InputRequired(),Length(min=4,message="Password min length is 4"), EqualTo('password', message='Passwords must match')])
    submit = SubmitField(label="Register")