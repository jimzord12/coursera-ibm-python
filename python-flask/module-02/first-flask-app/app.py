from flask import Flask, request
from Maths import summation
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1> Welcome to my 1st Flask Web Service! </h1>"

@app.route("/sum")
def sum_route():
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))
    return str(summation(num1, num2))