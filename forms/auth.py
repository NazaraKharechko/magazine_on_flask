from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, length, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])


class RegisterForm(FlaskForm):
    email = StringField('Email', [DataRequired(), length(3, 30, 'Email must be 3-30 characters')])
    number = StringField('Number', [DataRequired(), length(8, 10, 'Number must be 8-10 characters')])
    name = StringField('Name', [DataRequired(), length(0, 20, 'Name must be 0-20 characters')])
    password = PasswordField('Password', [DataRequired(), length(6, 20, 'Password must be 6-20 characters')])
    confirm = PasswordField('Confirm', [DataRequired(), EqualTo('password', 'Passwords is not equals'),
                                        length(6, 20, 'Password must be 6-20 characters')])
