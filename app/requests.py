import urllib.request,json
from .models import User

secret_key = None
database_uri = None

def configure_request(app):
    global secret_key,database_uri

    secret_key= app.config['SECRET_KEY']
    database_uri= app.config['SQLALCHEMY_DATABASE_URI']