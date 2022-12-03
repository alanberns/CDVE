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
from flask_cors import cross_origin
from werkzeug.utils import secure_filename
from src.web.helpers.uploads_path import getComprobantePath

api_blueprint = Blueprint("api", __name__, url_prefix="/api")


def token_required(f):
    """
    Esta funcion se utiliza como wrapper, y exije que la peticion realizada envie el token jwt
    Si el token caduco o no es valido, se envia el mensaje correspondiente.
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return jsonify({"message": "El token es invalido"}), 401
        try:
            data = jwt.decode(
                token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
            )
            user = board.get_usuario(data["id"])
        except:
            return jsonify({"message": "El token es invalido"}), 401
        return f(user, *args, **kwargs)

    return decorated


@cross_origin
@api_blueprint.post("/login")
def login():
    """
    Funcion que sirve para realizar el login, si se envia un usuario y contraseña validos dentro
    de la BD, entonces devuelve un token.
    """
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response(
            {"message": "Contraseña incorrecta"},
            401,
            {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
        )
    user = board.find_user_by_email(auth.username)
    if not user:
        return make_response(
            {"message": "El usuario no existe"},
            401,
            {'WWW-Authenticate': 'Basic realm ="User does not exist !!"'}
        )
    if not user.socio:
        return make_response(
            {"message": "El usuario no es un socio"},
            401,
            {'WWW-Authenticate': 'Basic realm ="User is not socio !!"'}
        )
    if user.verify_password(auth.password):
        token = jwt.encode(
            {"id": user.id, "exp": datetime.utcnow() + timedelta(minutes=30)},
            current_app.config["SECRET_KEY"],
            algorithm="HS256",
        )
        return jsonify({"token": token})
    return make_response(
        {"message": "Contraseña incorrecta"},
        401,
        {"WWW-Authenticate": "Basic Realm='Login Required!"}
    )


@cross_origin  # Sin esto no permite hacer la peticion localmente desde el front
@api_blueprint.get("/me/payments")
@token_required
def list_payments(current_user):
    """
    Funcion que devuelve el listado de pagos del usuario actual.
    """
    page = request.args.get("page", default=1, type=int)
    try:
        pagos = board.get_pagos_by_socio_id(current_user.socio[0].id, page)
    except KeyError:
        return jsonify({"message": "EL usuario actual no es un socio"}), 401

    payments = {
        "pages": pagos.pages,
        "current_page": pagos.page,
        "payments": [pago.serialize for pago in pagos.items],
    }
    return jsonify(payments)


@cross_origin
@api_blueprint.post("/me/payments")
@token_required
def pay(current_user):
    """
    Funcion que realiza un pago, recibe el nro_cuota, el monto y la disciplina que el usuario
    quiere pagar.
    Si el monto no es correcto devuelve un mensaje indicando el monto necesario.
    """
    cuotas = request.json["cuotas"]
    disciplina_nombre = request.json["disciplina"]
    cuotas_ids = []
    for c in cuotas:
        nro_cuota = c["month"]
        amount = c["amount"]
        try:
            amount = int(amount)
        except ValueError:
            return jsonify({"message": "El monto debe ser un numero"}), 401
        if not nro_cuota or not amount or not disciplina_nombre:
            return (
                jsonify({"message": "Los datos proporcionados no son correctos"}),
                401,
            )
        try:
            disciplina = board.find_disciplina_by_name(disciplina_nombre)
            inscripcion = board.get_inscripcion_by_socio_and_disciplina(
                current_user.socio[0], disciplina
            )
            cuota = board.get_cuota_by_inscripcion_id_and_nro_cuota(
                inscripcion.id, nro_cuota
            )
        except AttributeError:
            return (
                jsonify(
                    {"message": "La disciplina que intenta pagar esta inactiva"}),
                401,
            )
        except KeyError:
            return jsonify({"message": "El usuario actual no es un socio"}), 401
        if cuota.estado_pago:
            return jsonify({"message": f"Esta cuota ya se encuentra pagada."}), 401
        if not cuota.valor_cuota == amount:
            return (
                jsonify(
                    {
                        "message": f"Para realizar el pago necesita un monto de {cuota.valor_cuota}"
                    }
                ),
                401,
            )
        cuotas_ids.append(cuota.id)
    pago = board.generate_payment(cuotas_ids)
    return jsonify(payments=pago.serialize)


@cross_origin
@api_blueprint.get("/club/info")
def info_club():
    """
    Funcion que devuelve el email y numero de telefono del club.
    """
    config = board.list_configuracion()
    return jsonify(info=config.serialize_info_club)


@cross_origin
@api_blueprint.get("/club/disciplines")
def get_disciplines():
    """
    Devuelve las disciplinas activas del club
    """
    page = request.args.get("page", default=1, type=int)
    disciplines = board.list_disciplinas_activas(page)
    disciplinas = []
    for discipline in disciplines.items:
        disc = {
            "name": discipline.nombre,
            "categoria": discipline.categoria,
            "teacher": discipline.entrenador,
            "days": discipline.dia,
            "time": discipline.hora,
            "costo_mensual": discipline.costo_mensual,
        }
        disciplinas.append(disc)
    data = {
        "pages": disciplines.pages,
        "current_page": disciplines.page,
        "data": disciplinas,
    }
    return data


@cross_origin
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
        "first_name": usuario.first_name,
        "last_name": usuario.last_name,
    }
    usuario_data = jsonify(user_data)
    return usuario_data


@cross_origin
@api_blueprint.get("/statistics/inscripcionesPorDisciplina")
@token_required
def get_statistics_inscripcionesPorDisciplina(current_user):
    """
    Devuelve las disciplinas y sus inscriptos
    """
    disciplinas = board.list_all_disciplinas_activas()
    data = []
    for disciplina in disciplinas:
        d = {
            "nombre": disciplina.nombre + " " + disciplina.categoria,
            "num_socios": len(disciplina.socio),
        }
        data.append(d)
    return data


@api_blueprint.get("/me/license")
@token_required
def get_socio_state(current_user):
    """
    Devuelve la información de un socio y su estado de credencial
    """
    usuario = board.get_usuario(current_user.id)
    socio = board.find_socio_by_id_usuario(current_user.id)
    user_data = {
        "status": "",
        "description": "",
        "profile": {
            "user": usuario.username,
            "email": usuario.email,
            "number": socio.id,
            "document_type": socio.tipo_documento,
            "document_number": socio.numero_documento,
            "gender": socio.genero,
            "address": socio.direccion,
            "phone": socio.telefono,
        },
    }
    if not board.es_moroso(socio.id):
        user_data["description"] = "El socio no registra deuda ni sanción."
        user_data["status"] = "OK"
    else:
        user_data["description"] = "El socio es moroso."
        user_data["status"] = "NOT OK"
    usuario_data = jsonify(user_data)
    return usuario_data


@cross_origin
@api_blueprint.get("/statistics/concurrencia")
@token_required
def get_statistics_concurrencia(current_user):
    """
    Retorna la cantidad de personas que asisten al club por hora
    """
    horas = [
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
    ]
    hora_data = []
    cantidad = []
    for hora in horas:
        hora_data.append(hora)
        disciplinas = board.get_disciplinas_time(hora)
        c = 0
        for disciplina in disciplinas:
            c = c + len(disciplina.socio)
        cantidad.append(c)
    data = {
        "hora": hora_data,
        "personas": cantidad,
    }

    return data


@cross_origin
@api_blueprint.get("/statistics/genero")
@token_required
def get_statistics_genero(current_user):
    """
    Retorna la cantidad de socios por genero
    """
    generos = []
    valores = {}
    socios = board.list_socios_all()
    for socio in socios:
        if socio.genero not in generos:
            generos.append(socio.genero)
            valores[socio.genero] = 1
        else:
            valores[socio.genero] = valores[socio.genero] + 1
    cantidades = []
    for genero in generos:
        cantidades.append(valores[genero])
    data = {
        "genero": generos,
        "cantidad": cantidades,
    }
    return data


def _allowed_file(filename):
    """
    Verifica que el archivo sea pdf, jpg o png
    """
    ALLOWED_EXTENSIONS = set(["pdf", "png", "jpg"])
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@cross_origin
@api_blueprint.post("/me/comprobante")
@token_required
def comprobante(current_user):
    """
    Funcion que recibe y guarda el comprobante enviado desde el frontend.
    """
    pago_id = request.form["id"]
    if "file" not in request.files:
        return jsonify({"message": "Archivo no encontrado en la peticion"}), 400
    file = request.files["file"]
    filename = secure_filename(file.filename)
    if not _allowed_file(filename):
        return jsonify({"message": "El archivo debe ser jpg, png o pdf"}), 400
    filepath = getComprobantePath(filename)
    file.save(filepath)
    board.set_comprobante_by_pago_id(pago_id, filename)
    return jsonify({"message": f"Comprobante guardado satisfactoriamente"}), 200


@cross_origin
@api_blueprint.get("/me/disciplines")
@token_required
def me_get_disciplines(current_user):
    """
    Devuelve las disciplinas activas  del usuario
    """
    disciplines = board.get_disciplinas_by_user_id(current_user.socio[0].id)
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
    data = {
        "data": disciplinas,
    }
    return data


@cross_origin
@api_blueprint.get("/me/cuotas")
@token_required
def me_get_cuotas(current_user):
    """
    Devuelve las disciplinas activas  del usuario
    """
    disciplina = request.args.get("disciplina")
    disciplina = board.find_disciplina_by_name(disciplina)
    inscripcion = board.get_inscripcion_by_socio_and_disciplina(
        current_user.socio[0], disciplina
    )
    cuotas = board.get_cuotas_adeudadas_by_inscripcion_id(inscripcion.id)
    return jsonify(cuotas=[cuota.serialize for cuota in cuotas])
