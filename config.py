import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')

    ID = os.environ.get("CLIENT_ID")

    SECRET = os.environ.get("SECRET")

