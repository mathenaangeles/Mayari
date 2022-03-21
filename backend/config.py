import os
class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://") # 'sqlite:///mayari.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'whorunthehelloworld'
    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    REGION_NAME = os.environ.get('REGION_NAME')