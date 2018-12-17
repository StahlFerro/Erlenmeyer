from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from server.models import Engine


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class EngineForm(ModelForm):
    class Meta:
        model = Engine
