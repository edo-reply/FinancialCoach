from flask import jsonify, request

from app import app
from services import user_service

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user is not None:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if data:
        user = user_service.create_user(data)
        return jsonify(user), 201
    else:
        return jsonify({'error': 'Invalid data'}), 400

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_service.delete_user(user_id):
        return jsonify({'message': 'User deleted'}), 204
    else:
        return jsonify({'error': 'User not found'}), 404
