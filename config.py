import os


basedir = os.path.abspath(os.path.dirname(__file__))

sqlite_url = f"sqlite:///{os.path.join(basedir, 'data.db')}"
postgres_url = f"postgresql://postgres@localhost:5432/IMVR_DATA"


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sushi'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or postgres_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def is_list(obj_type):  # Jinja custom test to determine whether a variable is a list
    if obj_type is list:
        return True
    else:
        return False
