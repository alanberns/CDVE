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
def list_payments(current_user):
    try:
        pagos = board.get_pagos_by_socio_id(current_user.socio[0].id)
    except KeyError:
        return jsonify({"message": "EL usuario actual no es un socio"}), 401
    return jsonify(payments=[pago.serialize for pago in pagos])


# @api_blueprint.post("/me/payments")
# @token_required
# def pay(current_user):
#     month = request.json[0]["month"]
#     amount = request.json[0]["amount"]
#     if not month or not amount:
#         return jsonify({"message": "Los datos proporcionados no son correctos"}), 401
#     try:
#         cuotas = board.get_cuotas_by_socio_id_and_nro_cuota(
#             current_user.socio[0].id, month)
#     except KeyError:
#         return jsonify({"message": "EL usuario actual no es un socio"}), 401
#     if not cuotas.valor_cuota == amount:
#         return jsonify({"message": f"Para realizar el pago necesita un monto de cuotas.valor_cuota"}), 401
#     pagos = board.generate_payment([cuotas.id])
#     return jsonify(payments=[pago.serialize for pago in pagos])

@api_blueprint.get("/club/disciplines")
def get_disciplines():
    disciplines = board.list_disciplinas()
    disciplinas = []
    for discipline in disciplines:
        disc = {
            "nombre": discipline.nombre,
            "categoria": discipline.categoria,
            "entrenador": discipline.entrenador,
            "dia": discipline.dia,
            "hora": discipline.hora,
            "costo_mensual": discipline.costo_mensual,
        }
        disciplinas.append(disc)
    disciplinas = jsonify(disciplinas)
    return disciplinas