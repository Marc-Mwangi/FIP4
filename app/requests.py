
secret_key = None
database_uri = None

base_url ='http://quotes.stormconsultancy.co.uk/random.json '

def configure_request(app):
    global secret_key,database_uri

    

    secret_key= app.config['SECRET_KEY']
    database_uri= app.config['SQLALCHEMY_DATABASE_URI']