from flask import Flask
from .extensions import db, api
from dotenv import load_dotenv
import os
from app.controllers.user_controller import ns as user_ns
# Load environment variables from .env file
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Load configuration from environment variables
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    db.init_app(app)
    api.init_app(app)

    # Register namespaces

    api.add_namespace(user_ns, path='/users')

    return app