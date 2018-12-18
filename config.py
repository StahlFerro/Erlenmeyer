import os


basedir = os.path.abspath(os.path.dirname(__file__))

sqlite_url = f"sqlite:///{os.path.join(basedir, 'data.db')}"
postgres_url = f"postgresql://postgres@localhost:5432/IMVR_DATA"


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sushi'
    JWT_SECRET_KEY = 'laksa'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or postgres_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']


def is_list(obj_type):  # Jinja custom test to determine whether a variable is a list
    if obj_type is list:
        return True
    else:
        return False


JINJA_GLOBALS = {
    'type': type,
    'enumerate': enumerate,
}

JINJA_TESTS = {
    'is_list': is_list,
}