from flask import Flask, jsonify
from database import db

app = Flask(__name__)


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal Server Error"}), 500


@app.route("/api/version")
def version():
    return "1.0"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

db.init_app(app)
with app.app_context():
    db.create_all()
    print('[INFO] ')

if __name__ == '__main__':
    from controllers.user_controller import *
    from controllers.transaction_controller import *
    from controllers.advice_controller import *

    app.run()
