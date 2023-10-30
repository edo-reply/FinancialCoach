from flask import jsonify, request

from app import app
from services import user_service
from models.user import User


@app.get('/api/users/<string:user_id>')
def get_user(user_id: int):
    print("req:", user_id)
    user = user_service.get_user(user_id)
    if user is not None:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404


@app.post('/api/users')
def create_user():
    body = request.get_json(silent=True)
    if body:
        try:
            user = User(**body)
        except TypeError as err:
            print(type(err))
            return jsonify({"error": "Invalid request"}), 400
    else:
        return jsonify({"error": "Unsupported media type"}), 415

    user = user_service.create_user(user)
    return jsonify(user), 201


@app.delete('/api/users/<string:user_id>')
def delete_user(user_id: int):
    if user_service.delete_user(user_id):
        return None, 204
    else:
        return jsonify({'error': 'User not found'}), 404
