from pprint import pprint

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, validators
from wtforms.validators import DataRequired
from wtforms_alchemy import model_form_factory, QuerySelectField, NumberRange

from server import db
from server.models import Ship, Engine, Builder, ShipType, ShipStatus, User
from server.utils.orm import get_m2o_columns

BaseModelForm = model_form_factory(FlaskForm)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session

    def __init__(self, *args, **kwargs):
        """ This is an override to replace integer fields with unsigned ones specified in the model's
            unsigned_attrs() method """
        super(ModelForm, self).__init__(*args, **kwargs)
        # print('--->', self.Meta.model)
        if self.Meta.model:
            model = self.Meta.model
            m2o_rels = get_m2o_columns(model)
            # print('--> model', model)
            # print('--> model')
            # pprint(m2o_rels)
            try:
                unsigned_attrs = model.unsigned_attrs()
            except AttributeError:
                unsigned_attrs = None
            if unsigned_attrs:
                for uatrs in unsigned_attrs:
                    """ 'self.__class__' here is the derived class (ex: ShipForm class) """
                    setattr(self.__class__, uatrs, IntegerField(validators=[NumberRange(min=0)]))
                    # print('getattr', getattr(self.__class__, uatrs))

            # if m2o_rels:
            #     for col, modelclass in m2o_rels.items():
            #         print('--->', col)
            #         qlambda = lambda: modelclass.query
            #         print('-->', qlambda().all())
            #         setattr(self.__class__, col, QuerySelectField(query_factory=qlambda, allow_blank=True))


class UserForm(ModelForm):
    class Meta:
        model = User
        

class LoginForm(ModelForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')


class UpdatePasswordForm(ModelForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', [validators.Length(min=10, max=100)])


def engine_query():
    return Engine.query


def ship_type_query():
    return ShipType.query


def ship_status_query():
    return ShipStatus.query


def builder_query():
    return Builder.query


def ship_query():
    return Ship.query


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


class ShipForm(ModelForm):
    class Meta:
        model = Ship
        date_format = '%Y-%m-%d'

    engine = QuerySelectField(query_factory=engine_query, allow_blank=True)
    builder = QuerySelectField(query_factory=builder_query, allow_blank=True)
    ship_type = QuerySelectField(query_factory=ship_type_query, allow_blank=True)
    ship_status = QuerySelectField(query_factory=ship_status_query, allow_blank=True)
