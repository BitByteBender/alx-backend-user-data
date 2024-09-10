#!/usr/bin/env python3
""" Basic flask app creation
"""
from flask import Flask, jsonify, request, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """ Basic route:
        returns a welcoming message
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """ POST Route /users
        Registers a new user using email and password
        Return: Created account with user credentials
    """
    email = request.form.get("email")
    password = request.form.get("password")

    # if not email or not password:
    # return jsonify({"message": "Missing email or password"}), 400

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """ Handles user login and session creation
        Returns:
        json payload of the form
    """
    email = request.form.get("email")
    password = request.form.get("password")

    valid_user = AUTH.valid_login(email, password)
    if not valid_user:
        abort(401)

    session_id = AUTH.create_session(email)
    res = jsonify({"email": email, "message": "logged in"})
    res.set_cookie("session_id", session_id)
    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
