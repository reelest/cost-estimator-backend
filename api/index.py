from flask import Flask
from prefix_middleware import PrefixMiddleware
app = Flask(__name__)
app.debug = True
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix="/api")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
