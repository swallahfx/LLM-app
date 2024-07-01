from dotenv import load_dotenv
from flask import Flask

from .routers.ask_router import api_blueprint

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
