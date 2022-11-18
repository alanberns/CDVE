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
    """
    Esta funcion se utiliza como wrapper, y exije que la peticion realizada envie el token jwt
    Si el token caduco o no es valido, se envia el mensaje correspondiente.
    """
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
    """
    Funcion que sirve para realizar el login, si se envia un usuario y contraseña validos dentro
    de la BD, entonces devuelve un token.
    """
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
    """
    Funcion que devuelve el listado de pagos del usuario actual.
    """
    try:
        pagos = board.get_pagos_by_socio_id(current_user.socio[0].id)
    except KeyError:
        return jsonify({"message": "EL usuario actual no es un socio"}), 401
    return jsonify(payments=[pago.serialize for pago in pagos])


@api_blueprint.post("/me/payments")
@token_required
def pay(current_user):
    """
    Funcion que realiza un pago, recibe el nro_cuota, el monto y la disciplina que el usuario
    quiere pagar.
    Si el monto no es correcto devuelve un mensaje indicando el monto necesario.
    """
    nro_cuota = request.json[0]["month"]
    amount = request.json[0]["amount"]
    disciplina = request.json[0]["disciplina"]
    try:
        amount = int(amount)
    except ValueError:
        return jsonify({"message": "El monto debe ser un numero"}), 401
    if not nro_cuota or not amount or not disciplina:
        return jsonify({"message": "Los datos proporcionados no son correctos"}), 401
    try:
        disciplina = board.find_disciplina_by_name(disciplina)
        inscripcion = board.get_inscripcion_by_socio_and_disciplina(
            current_user.socio[0], disciplina)
        cuota = board.get_cuota_by_inscripcion_id_and_nro_cuota(
            inscripcion.id, nro_cuota)
    except AttributeError:
        return jsonify({"message": "La disciplina que intenta pagar esta inactiva"}), 401
    except KeyError:
        return jsonify({"message": "El usuario actual no es un socio"}), 401
    if cuota.estado_pago:
        return jsonify({"message": f"Esta cuota ya se encuentra pagada."}), 401
    if not cuota.valor_cuota == amount:
        return jsonify({"message": f"Para realizar el pago necesita un monto de {cuota.valor_cuota}"}), 401
    pago = board.generate_payment([cuota.id])
    return jsonify(payments=pago.serialize)


@api_blueprint.get("/club/info")
def info_club():
    """
    Funcion que devuelve el email y numero de telefono del club.
    """
    config = board.list_configuracion()
    return jsonify(info=config.serialize_info_club)


@api_blueprint.get("/club/disciplines")
def get_disciplines():
    """
    Devuelve las disciplinas del club
    """
    disciplines = board.list_disciplinas()
    disciplinas = []
    for discipline in disciplines:
        disc = {
            "name": discipline.nombre,
            "categoria": discipline.categoria,
            "teacher": discipline.entrenador,
            "days": discipline.dia,
            "time": discipline.hora,
            "costo_mensual": discipline.costo_mensual,
        }
        disciplinas.append(disc)
    disciplinas = jsonify(disciplinas)
    return disciplinas

@api_blueprint.get("/me/profile")
@token_required
def get_user_info(current_user):
    """
    Devuelve la información del usuario logueado
    """
    usuario = board.get_usuario(current_user.id)
    socio = board.find_socio_by_id_usuario(current_user.id)
    user_data = {
        "user": usuario.username,
        "email": usuario.email,
        "number": socio.id,
        "document_type": socio.tipo_documento,
        "document_number": socio.numero_documento,
        "gender": socio.genero,
        "address": socio.direccion,
        "phone": socio.telefono,
    }
    usuario_data = jsonify(user_data)
    return usuario_data
