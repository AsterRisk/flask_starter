import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    SQL_DATABASE_ADDRESS = '127.0.0.1' or 'localhost'
    DATABASE_NAME = 'properties'
    UPLOAD_FOLDER = "app/uploads/"
    TEMPLATE_FOLDER = "app/templates/"
    STATIC_FOLDER = "app/static/"
    SQLALCHEMY_USERNAME = 'postgres'
    SQLALCHEMY_PASSWORD =  '7931_Latias_1828'
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROJECT_DATABASE_URL') or 'postgresql://{}:{}@{}/{}'.format(SQLALCHEMY_USERNAME, SQLALCHEMY_PASSWORD, SQL_DATABASE_ADDRESS, DATABASE_NAME)

    print("\nDatabase URI: {}\n".format(SQLALCHEMY_DATABASE_URI))
    
    #SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False