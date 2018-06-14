import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    #Use environment key for production, or hardcoded key for local developement
    SECRET_KEY = os.environ.get('SECRET_KEY') or '0xtzMPvy1mhXypSG90Y5rsW0yDdKraTZ'

    #Use environment key for database connection, or SQLite db for local developement
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
