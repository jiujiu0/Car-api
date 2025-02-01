from flask import Blueprint, jsonify

account = Blueprint('account', __name__)


@account.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "User API is working"})
