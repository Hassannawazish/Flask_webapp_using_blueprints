from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField


class AddForm(FlaskForm):
    user_name = StringField('Enter your Name: ')
    suggestion = StringField('Enter your suggestion: ')
    submit = SubmitField('Submit')
