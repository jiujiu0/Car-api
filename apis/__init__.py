from flask import Blueprint
from AccountController import account


def register_api_routes(app):
    app.register_blueprint(account, url_prefix='/api/account')
