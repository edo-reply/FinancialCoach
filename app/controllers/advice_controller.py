from flask import jsonify

from app import app
from services import advice_service


@app.get("/api/users/<string:user_id>/advices")
def get_advice(user_id: str):
    advices = advice_service.get_advices(user_id)
    if advices is not None:
        return jsonify(advices)
    else:
        return jsonify({"error": "User not found"}), 404
