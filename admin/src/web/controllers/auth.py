from core.board import Usuario
from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from flask import session

from src.core import board



auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

@auth_blueprint.get("/")
def login():
    return render_template("auth/login.html")

@auth_blueprint.post("/authenticate")
def authenticate():
    params = request.form
    user = board.find_user_by_mail(params["email"])
    if not user or not user.verify_password(params['contraseña']):
        flash("email o clave incorrecta","danger")
        return redirect(url_for("auth.login"))
    session["user"] = user.mail
    flash("Se Ha iniciado la sesion correctamente","success")
    return redirect(url_for("usuarios.usuario_index"))


@auth_blueprint.get("/logout")
def logout():
    del session["user"]
    session.clear()
    flash("La sesion se cerro correctamente","success")
    return redirect(url_for("auth.login"))

@auth_blueprint.get("/register")
def register():
    pass
