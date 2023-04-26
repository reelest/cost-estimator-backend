from flask import Flask, request, abort,jsonify
from flask_cors import CORS

from ._utils.predict import predict

app = Flask(__name__)
CORS(app)

@app.post("/")
def get_cost_map():
    content_type = request.headers.get('Content-Type')
    if content_type and 'application/json' in content_type:
        return predict(request.json)
    else:
        abort(401, 'Content-Type not supported!')

app.get("/")
def status():
    return "Server is running"