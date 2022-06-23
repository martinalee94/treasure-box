import os

from app.main import create_app, blueprint
from flask_restx import Api

app = create_app(os.getenv('PROD_ENV') or 'dev')

app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(port=5000)