from flask import Blueprint
from flask import render_template
from flask import request
from pathlib import Path
from flask import redirect
from flask import url_for
from flask import flash
from datetime import datetime
from flask import session

from src.core import board
from src.web.helpers.auth import login_required
from src.core.forms.usuarios_form import ModificarUsuarioForm
from src.core.forms.usuarios_form import CambiarClaveForm


perfil_blueprint = Blueprint(
    "perfil", __name__, url_prefix="/MiPerfil")


@perfil_blueprint.get("/")
@login_required
def show_perfil():
    """
    Ver los datos del perfil
    """
    usuario_email = session["user"]
    usuario = board.find_user_by_email(usuario_email)
    form = ModificarUsuarioForm()
    form.set_from_usuarios(usuario)
    return render_template("perfil/perfil.html", form=form, usuario=usuario)

@perfil_blueprint.post("/")
@login_required
def modify_perfil():
    """
    #Modifica los datos del perfil
    """
    form = ModificarUsuarioForm(request.form)

    if not form.validate:
        flash("No se pudo modificar los datos", "danger")
        return redirect(url_for('perfil.show_perfil'))

    # Comprobar si se modificó el email
    if (form.email.data != usuario.email):
        # Si se modificó, comprobar que el nuevo email no esté en uso
        if (board.exist_email(form.email.data)):
            flash("el email ingresado ya esta registrado", "danger")
            return redirect(url_for('perfil.show_perfil'))

    # Comprobar si se modificó el username
    if (form.username.data != usuario.username):
        # Si se modificó, comprobar que el nuevo username no esté en uso
        if (board.exist_username(form.username.data)):
            flash("el username ingresado ya está registrado", "danger")
            return redirect(url_for('perfil.show_perfil'))
    
    kwargs = {
        "id": form.id.data,
        "email": form.email.data,
        "username": form.username.data,
        "updated_at": datetime.now(),
        "first_name": form.first_name.data,
        "last_name": form.last_name.data,
    }
    board.update_usuario(**kwargs)
    flash("Se actualizaron los datos del perfil", "success")
    return redirect(url_for('perfil.show_perfil'))

@perfil_blueprint.get("/CambiarClave")
@login_required
def change_password_view():
    """
    Ingresar a vista para cambiar la contraseña
    """
    form = CambiarClaveForm()
    return render_template("perfil/CambiarClave.html", form=form)

@perfil_blueprint.post("/CambiarClave")
@login_required
def change_password():
    """
    Modificar la contraseña
    """
    form = CambiarClaveForm(request.form)
    if not form.validate:
        flash("No se pudo validar las claves ingresadas", "danger")

    # Chequear la contraseña actual
    usuario_email = session["user"]
    usuario = board.find_user_by_email(usuario_email)
    if not usuario.verify_password(form.password_ant.data):
        flash("Contraseña incorrecta", "danger")
        return (redirect(url_for('perfil.change_password_view')))

    # Contraseñas deben coincidir. No funciona EqualTo
    if not form.password_nueva == form.password_repetir:
        flash("Las contraseñas deben coincidir", "danger")
        return (redirect(url_for('perfil.change_password_view')))

    # modificar la contraseña
    kwargs = {
        "id": usuario.id,
        "password": form.password_nueva.data,
    }
    board.update_password(**kwargs)
    flash("Se cambió su contraseña", "success")
    return (redirect(url_for('perfil.change_password_view')))