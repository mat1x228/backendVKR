from flask import Blueprint, request, jsonify
from api.database_module import get_users, get_user_by_id

messages_bp = Blueprint('messages', __name__)

@messages_bp.route('/messages', methods=['POST'])
def receive_message():
    message = request.get_json()
    process_message(message)
    return "Message received"

@messages_bp.route('/users', methods=['GET'])
def get_users_list():
    users = get_users()
    return jsonify(users)

@messages_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user)
    else:
        return "User not found", 404



