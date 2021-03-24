import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    SQL_DATABASE_ADDRESS = '127.0.0.1' or 'localhost'
    DATABASE_NAME = 'info3180_project'
    UPLOAD_FOLDER = "app/uploads/"
    TEMPLATE_FOLDER = "app/templates/"
    STATIC_FOLDER = "app/static/"
    SQLALCHEMY_USERNAME = os.environ.get('PROJECT_DATABASE_USERNAME') or 'root'
    SQLALCHEMY_PASSWORD =  os.environ.get('PROJECT_DATABASE_PASSWORD') or ''
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROJECT_DATABASE_URL') or 'mysql://{}:{}@{}/{}'.format(SQLALCHEMY_USERNAME, SQLALCHEMY_PASSWORD, SQL_DATABASE_ADDRESS, DATABASE_NAME)

    print("\nDatabase URI: {}\n".format(SQLALCHEMY_DATABASE_URI))
    
    #SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False