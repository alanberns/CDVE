from functools import wraps
from flask import abort
from flask import session

from src.core.board import find_user_by_email

def user_delete_req(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        permisos = []
        usuario = find_user_by_email(session.get("user"))
        for rol in usuario.roles:
            for permiso in rol.permisos:
                permisos.append(permiso.nombre)
        if "user_delete" not in permisos:
            abort(403)
        return f(*args,**kwargs)
    return decorated_function

def user_create_req(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        permisos = []
        usuario = find_user_by_email(session.get("user"))
        for rol in usuario.roles:
            for permiso in rol.permisos:
                permisos.append(permiso.nombre)
        if "user_create" not in permisos:
            abort(403)
        return f(*args,**kwargs)
    return decorated_function

def user_index_req(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        permisos = []
        usuario = find_user_by_email(session.get("user"))
        for rol in usuario.roles:
            for permiso in rol.permisos:
                permisos.append(permiso.nombre)
        if "user_index" not in permisos:
            abort(403)
        return f(*args,**kwargs)
    return decorated_function

def user_show_req(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        permisos = []
        usuario = find_user_by_email(session.get("user"))
        for rol in usuario.roles:
            for permiso in rol.permisos:
                permisos.append(permiso.nombre)
        if "user_show" not in permisos:
            abort(403)
        return f(*args,**kwargs)
    return decorated_function

def user_update_req(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        permisos = []
        usuario = find_user_by_email(session.get("user"))
        for rol in usuario.roles:
            for permiso in rol.permisos:
                permisos.append(permiso.nombre)
        if "user_update" not in permisos:
            abort(403)
        return f(*args,**kwargs)
    return decorated_function

def user_rol_update_req(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        permisos = []
        usuario = find_user_by_email(session.get("user"))
        for rol in usuario.roles:
            for permiso in rol.permisos:
                permisos.append(permiso.nombre)
        if "user_rol_update" not in permisos:
            abort(403)
        return f(*args,**kwargs)
    return decorated_function