from flask import request, jsonify
import requests
from service import clean_and_transform
from config import URL
from app import app  

@app.post('/clean')
def clean_endpoint():
    processed = clean_and_transform(request.json)

    requests.post(URL, json=processed)

    return jsonify({"status": "ok"})
