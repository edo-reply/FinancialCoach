from flask import Flask, jsonify

from controllers import user_controller
from controllers import transaction_controller
from controllers import insight_controller
from database import db


app = Flask(__name__)

app.register_blueprint(user_controller.bp)
app.register_blueprint(transaction_controller.bp)
app.register_blueprint(insight_controller.bp)


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'error': 'Internal Server Error'}), 500


@app.route('/api/version')
def version():
    return '1.0'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
