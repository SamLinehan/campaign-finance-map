import os
from os.path import join, dirname
from flask import Flask, jsonify
import requests
import json
from flask.ext.cors import CORS
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

CORS(app, resources={r'/*' : {"origins": "*"}}, allow_headers='Content-Type')

@app.route("/")
def hello():
    return "Welcome to the Campaign Finance Map"

@app.route("/candidates")
def get_candidates():
    key = os.environ.get("CAMPAIGN_FINANCE_API_KEY")
    url = os.environ.get("TEST_URL")
    headers = {
        'X-API-Key': key
    }
    data = requests.get(url, headers=headers)
    print (data.json())
    return jsonify(data.json())
    # return jsonify([{'firstName': 'Sam', 'lastName': 'Linehan'}])


if __name__ == "__main__":
    app.run(threaded=True)
