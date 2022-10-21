from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from flask import session

from src.core.forms.auth_form import AuthForm
from src.core import board


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.get("/")
def login():
    form = AuthForm(request.form)
    return render_template("auth/login.html", form=form)


@auth_blueprint.post("/authenticate")
def authenticate():
    form = AuthForm(request.form)
    user = board.find_user_by_email(form.email.data)
    if not form.validate:
        flash("Error validando los datos, por favor intenta otra vez", "danger")
    if not user or not user.verify_password(form.contraseña.data):
        flash("email o clave incorrecta", "danger")
        return redirect(url_for("auth.login"))
    
    # Validar que el usuario este activo para iniciar sesion
    if not user.activo:
        flash("No puede acceder al sistema: usuario inactivo", "danger")
        return redirect(url_for("auth.login"))
    session["user"] = form.email.data
    # session["permisos"] = board.user_get_permisos(user.id)
    flash("Se ha iniciado la sesion correctamente", "success")
    return redirect(url_for("home"))


@auth_blueprint.get("/logout")
def logout():
    del session["user"]
    session.clear()
    flash("La sesion se cerro correctamente", "success")
    return redirect(url_for("auth.login"))


@auth_blueprint.get("/register")
def register():
    pass
