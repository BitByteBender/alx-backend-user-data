#!/usr/bin/env python3
""" Basic flask app creation
"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", method=["GET"], strict_slashes=False)
def index() -> str:
    """ Basic route:
        returns a welcoming message
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
