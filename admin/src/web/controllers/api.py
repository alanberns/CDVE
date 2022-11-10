from flask import Blueprint
from flask import request
from flask import make_response
from src.core import board
from flask import jsonify
import jwt
from datetime import datetime
from datetime import timedelta
from flask import current_app

api_blueprint = Blueprint("api", __name__, url_prefix="/api")


@api_blueprint.post("/login")
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response("Could not verify", 401, {"WWW-Authenticate": "Basic Realm='Login Required!"})
    user = board.find_user_by_email(auth.username)
    if not user:
        return make_response("Could not verify", 401, {"WWW-Authenticate": "Basic Realm='Login Required!"})
    if user.verify_password(auth.password):
        token = jwt.encode(
            {"id": user.id, "exp": datetime.utcnow() + timedelta(minutes=3)}, current_app.config["SECRET_KEY"])
        return jsonify({"token": token})
    return make_response("Could not verify", 401, {"WWW-Authenticate": "Basic Realm='Login Required!"})
