from flask import Blueprint
from flask import request
from flask import make_response
from src.core import board
from flask import jsonify
import jwt
from datetime import datetime
from datetime import timedelta
from flask import current_app
from functools import wraps

api_blueprint = Blueprint("api", __name__, url_prefix="/api")


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        if not token:
            return jsonify({"message": "El token es invalido"}), 401
        try:
            data = jwt.decode(
                token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            user = board.get_usuario(data["id"])
        except:
            return jsonify({"message": "El token es invalido"}), 401
        return f(user, *args, **kwargs)
    return decorated


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
            {"id": user.id, "exp": datetime.utcnow() + timedelta(minutes=30)},
            current_app.config["SECRET_KEY"],
            algorithm="HS256"
        )
        return jsonify({"token": token})
    return make_response("Could not verify", 401, {"WWW-Authenticate": "Basic Realm='Login Required!"})


@api_blueprint.get("/me/payments")
@token_required
def list_payents(current_user):
    try:
        pagos = board.get_pagos_by_socio_id(current_user.socio[0].id)
    except KeyError:
        return jsonify({"message": "EL usuario actual no es un socio"}), 401
    return jsonify(payments=[pago.serialize for pago in pagos])
