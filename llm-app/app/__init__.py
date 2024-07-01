import os
from flask import Flask
from .routers.ask_router import api_blueprint

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()



def create_app():
    app = Flask(__name__)

    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
