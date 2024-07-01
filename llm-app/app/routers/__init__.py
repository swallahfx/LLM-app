from flask import Blueprint, jsonify
import os

from openai import OpenAI

api_blueprint = Blueprint('api', __name__)

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY", "")
    
)