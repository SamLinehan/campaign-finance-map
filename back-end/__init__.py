import os
from os.path import join, dirname
from flask import Flask, jsonify
import requests
import json
import threading
from flask.ext.cors import CORS
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

CORS(app, resources={r'/*' : {"origins": "*"}}, allow_headers='Content-Type')


candidate_data = {}

def get_data():
    threading.Timer(30.0, get_data).start()
    key = os.environ.get("CAMPAIGN_FINANCE_API_KEY")
    url = os.environ.get("CANDIDATE_URL")
    headers = {
        'X-API-Key': key
    }
    global candidate_data
    candidate_data = requests.get(url, headers=headers)
    return

get_data()

@app.route("/")
def hello():
    return "Welcome to the Campaign Finance Map"

@app.route("/candidates")
def get_candidates():
    print (candidate_data.json())
    return jsonify(candidate_data.json())


if __name__ == "__main__":
    app.run(threaded=True)
