from flask import Flask
from flask_restx import Api
from config import database
from route import company_route


app = Flask(__name__)
app.debug = 'development'
api = Api(app,
          version='1.0',
          title='Wanted API',
          doc='/swagger')


def add_namespace():
    api.add_namespace(company_route.api)

database.create_database(app)
add_namespace()


if __name__ == '__main__':
    app.run()
