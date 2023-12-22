from flask import Blueprint, jsonify

from services import insight_service

bp = Blueprint('insights', __name__)

@bp.get('/api/users/<string:user_id>/insights')
def get_insights(user_id: str):
    insights = insight_service.get_insights(user_id)
    if insights is not None:
        return jsonify(insights)
    else:
        return jsonify({'error': 'Not found'}), 404
