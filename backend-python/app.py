import datetime

from flask import Flask, request, jsonify
from flask_cors import CORS
from routers.requests import requests

app = Flask(__name__)
CORS(app)

app.register_blueprint(requests)


if __name__ == '__main__':
    app.run(port=5000)
