import os
from os.path import join, dirname
from flask import Flask, jsonify, request
from flask.ext.cors import CORS
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hi Sam!"

if __name__ == "__main__":
    app.run()
