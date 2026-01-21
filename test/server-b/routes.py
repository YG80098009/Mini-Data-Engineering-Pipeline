<<<<<<< HEAD
from flask import request, jsonify
=======
from fastapi import r
>>>>>>> service-b
import requests
from service import clean_and_transform
from main import app  

@app.post('/clean')
def clean_endpoint():
    Final_data = clean_and_transform(request.json)

    requests.post(json=Final_data)

    return jsonify({"status": "ok"})
