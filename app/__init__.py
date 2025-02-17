import logging

from dotenv import load_dotenv
from flask import Flask

from app.controllers.user_controller import ns as user_ns

from .extensions import api

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(level=logging.INFO)

def create_app():
    app = Flask(__name__)

    # Initialize API with a prefix
    api.init_app(app)

    # Register namespaces
    api.add_namespace(user_ns, path="/users")

    return app
