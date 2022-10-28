from functools import wraps
from flask import abort
from flask import session

from src.core.board import find_user_by_email
from src.web.helpers.auth import has_permission


def user_create_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not has_permission("user_create", session):
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


def user_index_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not has_permission("user_index", session):
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


def user_show_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not has_permission("user_show", session):
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


def user_update_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not has_permission("user_update", session):
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


def user_rol_update_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not has_permission("user_rol_update", session):
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


def config_all_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not has_permission("configuracion_all", session):
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


def pago_index_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not has_permission("pago_index", session):
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


def pago_show_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not has_permission("pago_show", session):
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


def socio_index_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not has_permission("socio_index", session):
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


def socio_update_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not has_permission("socio_update", session):
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


def socio_show_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not has_permission("socio_show", session):
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


def socio_create_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not has_permission("socio_create", session):
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


def socio_delete_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not has_permission("socio_delete", session):
            abort(403)
        return f(*args, **kwargs)
    return decorated_function