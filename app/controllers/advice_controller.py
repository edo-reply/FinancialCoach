from flask import Blueprint, jsonify

from services import advice_service

bp = Blueprint('advices', __name__)

@bp.get("/api/users/<string:user_id>/advices")
def get_advice(user_id: str):
    advices = advice_service.get_advices(user_id)
    if advices is not None:
        return jsonify(advices)
    else:
        return jsonify({"error": "Not found"}), 404
