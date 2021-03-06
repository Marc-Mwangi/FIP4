import os

class Config:
    """
    General configuraion
    """
    quote_api_base= 'http://quotes.stormconsultancy.co.uk/random.json '
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://marc:qwerty01@localhost/quote'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class Production(Config):
    """
    Production configuration
    """
    pass
class Development(Config):
    """
    Development configuration
    """
    DEBUG = True

config_options = {
    'development': Development ,
    'production': Production
}