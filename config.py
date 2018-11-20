import os
basedir = os.path.abspath(os.path.dirname(__file__))

sqlite_url = f"sqlite:///{os.path.join(basedir, 'data.db')}"
postgres_url = f"postgresql://postgres@localhost:5432/imvr_data"


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sushi'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or postgres_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
