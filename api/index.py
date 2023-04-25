from flask import Flask, request, abort
from ._utils.predict import predict

app = Flask(__name__)


@app.route("/")
def get_cost_map():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        return predict(request.json)
    else:
        abort(401, 'Content-Type not supported!')
