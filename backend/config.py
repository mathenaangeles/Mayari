class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///ilustrado.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'whorunthehelloworld'