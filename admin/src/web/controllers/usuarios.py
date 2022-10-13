from flask import Blueprint
from flask import render_template
from flask import request

from src.core import board


usuario_blueprint = Blueprint("usuarios", __name__, url_prefix="/usuarios")


@usuario_blueprint.get("/")
def usuario_index():
    usuarios = board.list_usuarios()
    return render_template("home.html", usuarios=usuarios)


@usuario_blueprint.get("/add")
def add_usuario_view():
    return render_template("nuevoUsuario.html")


@usuario_blueprint.post("/")
def add_usuario():
    kwargs = {
        "username": request.form.get("username"),
    }
    board.create_usuario(**kwargs)
    usuarios = board.list_usuarios()
    return render_template("home.html", usuarios=usuarios)
