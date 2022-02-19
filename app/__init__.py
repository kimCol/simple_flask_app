import os
from flask import Flask
from markupsafe import escape


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)

    @app.route("/")
    def hello():
        return "Hello, World!"

    @app.route('/user/<name>')
    def display_username(name):
        return f'User {escape(name)}'

    return app
