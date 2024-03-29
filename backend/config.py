import os
user = os.environ.get('POSTGRES_USER')
password = os.environ.get('POSTGRES_PASSWORD')
host = os.environ.get('POSTGRES_HOST')
database = os.environ.get('POSTGRES_DB')
port = os.environ.get('POSTGRES_PORT')
class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI =  'sqlite:///mayari.db' # f'postgresql://{user}:{password}@{host}:{port}/{database}' # 'sqlite:///mayari.db' # 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'whorunthehelloworld'
    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    REGION_NAME = os.environ.get('REGION_NAME')