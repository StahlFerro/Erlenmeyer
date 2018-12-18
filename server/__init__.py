from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager

from config import Config, is_list


app = Flask(__name__)
app.config.from_object(Config)
app.jinja_env.tests['is_list'] = is_list
app.jinja_env.globals['type'] = type
app.jinja_env.globals['enumerate'] = enumerate
api = Api(app)
jwt = JWTManager(app)
login = LoginManager(app)
login.login_view = '/login'
db = SQLAlchemy(app)
session = db.session
migrate = Migrate(app, db)

from server import routes, models, rest_api, utils
