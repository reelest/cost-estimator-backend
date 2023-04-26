from flask import Flask, request, abort,jsonify
from ._utils.predict import predict

app = Flask(__name__)


@app.route("/")
def get_cost_map():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        response = response = jsonify(predict(request.json))
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        abort(401, 'Content-Type not supported!')
