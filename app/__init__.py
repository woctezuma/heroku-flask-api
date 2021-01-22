from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS

app = Flask(__name__)
CORS(
    app,
    resources={
        r"/similar_apps_from_id": {"origins": ["woctezuma.github.io", "http://localhost:5000"]}
    },
)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["300 per hour", "30 per minute"]
)

from app import routes
