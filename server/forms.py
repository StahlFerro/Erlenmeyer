from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms_alchemy import model_form_factory

from server import db
from server.models import Engine, Builder, ShipType, ShipStatus


BaseModelForm = model_form_factory(FlaskForm)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session


class LoginForm(ModelForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')


class EngineForm(ModelForm):
    class Meta:
        model = Engine


class BuilderForm(ModelForm):
    class Meta:
        model = Builder


class ShipTypeForm(ModelForm):
    class Meta:
        model = ShipType


class ShipStatusForm(ModelForm):
    class Meta:
        model = ShipStatus
