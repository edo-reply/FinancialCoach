from uuid import uuid4

from flask import Blueprint, jsonify, request

from models import Transaction
from services import transaction_service


bp = Blueprint('transactions', __name__)

@bp.get("/api/users/<string:user_id>/transactions")
def get_transactions(user_id: str):
    transactions = transaction_service.get_transactions(user_id)
    if transactions is not None:
        return jsonify(transactions)
    else:
        return jsonify({"error": "Transactions not found"}), 404


@bp.post("/api/users/<string:user_id>/transactions")
def create_transaction(user_id: str):
    body = request.get_json(silent=True)
    if not body:
        return jsonify({"error": "Unsupported media type"}), 415

    try:
        transaction = Transaction(**body, id=str(uuid4()), user_id=user_id)
    except TypeError as err:
        print(err)
        return jsonify({"error": "Invalid request"}), 400

    transaction = transaction_service.create_transactions(transaction)

    if transaction is not None:
        return jsonify(transaction), 201
    else:
        return jsonify({"error": "User not found"}), 404

@bp.put("/api/users/<string:user_id>/transactions/<string:transaction_id>")
def update_transaction(user_id: str, transaction_id: str):
    body = request.get_json(silent=True)
    if not body:
        return jsonify({"error": "Unsupported media type"}), 415

    try:
        transaction = Transaction(**body, id=transaction_id, user_id=user_id)
    except TypeError as err:
        print(err)
        return jsonify({"error": "Invalid request"}), 400

    transaction = transaction_service.update_transactions(transaction)

    if transaction is not None:
        return jsonify(transaction), 201
    else:
        return jsonify({"error": "User not found"}), 404
