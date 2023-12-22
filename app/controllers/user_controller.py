from uuid import uuid4

from flask import Blueprint, jsonify, request

from models import User
from services import user_service

bp = Blueprint('users', __name__)

@bp.get('/api/users/<string:user_id>')
def get_user(user_id: str):
    user = user_service.get_user(user_id)
    if user is not None:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404


@bp.post('/api/users')
def create_user():
    body = request.get_json(silent=True)
    if not body:
        return jsonify({'error': 'Unsupported media type'}), 415

    try:
        user = User(**body, id=str(uuid4()))
    except TypeError as err:
        print(err)
        return jsonify({'error': 'Invalid request'}), 400

    user = user_service.create_user(user)
    return jsonify(user), 201


@bp.delete('/api/users/<string:user_id>')
def delete_user(user_id: str):
    if user_service.delete_user(user_id):
        return '', 204
    else:
        return jsonify({'error': 'User not found'}), 404
