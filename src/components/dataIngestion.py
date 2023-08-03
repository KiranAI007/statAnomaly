import os
import sys
from src.exception import CustomException
from src.logger import logging

from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Anomaly Detection"

@app.route('/catchData', methods = ['POST'])
def catchData():
    dataset = json.loads(request.data)
    print(dataset)
    return {'success':True}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)