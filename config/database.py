from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

_db_host = 'localhost'
_db_name = 'wanted_db'
_db_username = 'wanted'
_db_password = 'wanted'


def create_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + _db_username + ':' + _db_password + '@' + _db_host + ':3306/' + _db_name
    app.config['SQLALCHEMY_POOL_SIZE'] = 20
    app.config['SQLALCHEMY_POOL_TIMEOUT'] = 50
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 1800
    app.config['SQLALCHEMY_BINDS'] = {
        'reader': 'mysql+pymysql://' + _db_username + ':' + _db_password + '@' + _db_host + ':3306/' + _db_name,
        'cluster': 'mysql+pymysql://' + _db_username + ':' + _db_password + '@' + _db_host + ':3306/' + _db_name,
    }
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
