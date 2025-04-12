import datetime

from flask import Flask, request, jsonify
from flask_cors import CORS
from routers.requests import requests

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(requests)



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8888)
