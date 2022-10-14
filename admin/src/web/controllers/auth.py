from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for

from src.core import board



auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

@auth_blueprint.get("/")
def login():
    return render_template("auth/login.html")

@auth_blueprint.post("/authenticate")
def authenticate():
    params = request.form
    user = board.find_user_by_mail_and_pass(params["email"],params["contraseña"])
    if not user:
        flash("email o clave incorrecta","danger")
        return redirect(url_for("auth.login"))
    return redirect(url_for("usuarios.usuario_index"))


@auth_blueprint.get("/logout")
def logout():
    pass

