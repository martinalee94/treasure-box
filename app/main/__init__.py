from flask import Flask
from app.main.config import config_by_name
from flask import Flask, Blueprint
from flask_restx import Api
from app.main.dto.restaurant import api as restaurant_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint)

def add_api():
    api.add_namespace(restaurant_ns, path="/restaurants")

def create_app(config_by_name):
    app = Flask(__name__)
    add_api()

    return app