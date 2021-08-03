from flask_wtf import FlaskForm
from wtforms import StringField


class ChangeForm(FlaskForm):
    number = StringField('Phone number')
    name = StringField('Name')
