#!/usr/bin/python3
""" a script that starts a Flask web application:
the app is listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Return a string Hello HNBN"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns a string HNBN"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """display C followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))



@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """display Python followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
