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

@app.route("/")
def hello():
    return "Welcome to the Campaign Finance Map"

@app.route("/candidates")
def get_candidates():
    key = os.environ.get("CAMPAIGN_FINANCE_API_KEY")
    headers = {
        'X-API-Key': key
    }
    data = requests.get(CANDIDATE_URL, headers=headers)
    print (data.json())
    return jsonify(data.json())


if __name__ == "__main__":
    app.run(threaded=True)
