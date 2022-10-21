from flask import session
from functools import wraps
from flask import abort


def is_authenticated(session):
    return session.get("user") != None


# def has_permission(permission, session):
#     """
#     Funcion que retorna si un dado permiso se encuentra en el listado
#     de permisos de la sesión actual
#     """
#     return permission in session.get("permissions")


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user") is None:
            return abort(401)
        return f(*args, **kwargs)
    return decorated_function
