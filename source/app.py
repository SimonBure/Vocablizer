from flask import Flask, render_template, request, g

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
