from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager

from config import Config, is_list, JINJA_GLOBALS, JINJA_TESTS


app = Flask(__name__)
app.config.from_object(Config)
app.jinja_env.tests.update(JINJA_TESTS)
app.jinja_env.globals.update(JINJA_GLOBALS)
api = Api(app)
jwt = JWTManager(app)
login = LoginManager(app)
login.login_view = '/login'
db = SQLAlchemy(app)
session = db.session
migrate = Migrate(app, db)

from server import routes, user_routes, models, rest_api, utils
