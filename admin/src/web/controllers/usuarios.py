from flask import Blueprint
from flask import render_template
from flask import request
from pathlib import Path
from flask import redirect
from flask import url_for
from flask import flash
from datetime import datetime
import re

from src.core.forms.usuarios_form import UsuarioNuevoForm
from src.core.forms.usuarios_form import ModificarUsuarioForm
from src.core.forms.usuarios_form import BusquedaUsuarioForm
from src.core import board
from src.web.helpers.auth import login_required
from src.web.helpers.permissions.user_permission import (
    user_create_req,
    user_index_req,
    user_rol_update_req,
    user_update_req,
    user_show_req,
)


usuario_blueprint = Blueprint("usuarios", __name__, url_prefix="/usuarios")


@usuario_blueprint.get("/")
@login_required
@user_index_req
def usuario_index():
    """
    Menu inicial de usuarios: lista de usuarios
    """
    # Paginación
    form = BusquedaUsuarioForm()
    elementos_pagina = board.get_elementos_pagina()
    page = int(request.args.get("page", 1))
    email = request.args.get('email', default="")
    estado = request.args.get('estado', default="")
    if email != "" or estado != "":
        form.set_from_busqueda(email,estado)

    usuarios_pag = board.filter_usuarios(email, estado, page, elementos_pagina)
    return render_template(
        "usuarios/usuarios.html", usuarios_pag=usuarios_pag, form=form, email=email, estado=estado,
    )


@usuario_blueprint.post("/buscar")
@login_required
@user_index_req
def busqueda_filtrada():
    """
    Filtrar usuarios por email y estado.
    """
    # Obtener email y estado para la busqueda
    form = BusquedaUsuarioForm(request.form)
    if form.validate:
        estado = form.estado.data
        email = form.email.data

        return redirect(url_for('usuarios.usuario_index', email=email, estado=estado))
    else:
        flash("No se pudo realizar la busqueda","danger")
        return redirect(url_for('usuarios.usuario_index'))


@usuario_blueprint.get("/nuevo")
@login_required
@user_create_req
def add_usuario_view():
    """
    Vista para añadir un usuario
    """
    form = UsuarioNuevoForm()
    return render_template("usuarios/nuevoUsuario.html", form=form)


@usuario_blueprint.post("/nuevo")
@login_required
@user_create_req
def add_usuario():
    """
    Añadir usuario. Se necesita chequear que no se repita email ni username. Vuelve a menu usuarios
    """
    form = UsuarioNuevoForm(request.form)
    if form.validate:
        if board.exist_email(form.email.data):
            flash("El email ingresado ya está registrado", "danger")
            return redirect(url_for("usuarios.add_usuario_view"))
        if board.exist_username(form.username.data):
            flash("El username ingresado ya está registrado", "danger")
            return redirect(url_for("usuarios.add_usuario_view"))

        # Validar email
        if not validate_email(form.email.data):
            flash("Ingrese un email con un formato válido", "danger")
            return redirect(url_for("usuarios.add_usuario_view"))

        # Validar nombre, apellido y username
        if not validate_only_letters(form.username.data):
            flash("el nombre de usuario solo debe contener letras", "danger")
            return redirect(url_for("usuarios.add_usuario_view"))
        if not validate_only_letters(form.first_name.data):
            flash("el nombre solo debe contener letras", "danger")
            return redirect(url_for("usuarios.add_usuario_view"))
        if not validate_only_letters(form.last_name.data):
            flash("el apellido solo debe contener letras", "danger")
            return redirect(url_for("usuarios.add_usuario_view"))

        usuario = board.create_usuario(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            first_name=form.first_name.data,
            last_name=form.last_name.data,
        )
        flash("Se creó el nuevo usuario", "success")
        return redirect(url_for("usuarios.view_usuario", id=usuario.id))
    flash("No se pudo añadir al nuevo usuario", "danger")
    return redirect(url_for("usuarios.add_usuario_view"))


@usuario_blueprint.get("/<int:id>")
@login_required
@user_show_req
def view_usuario(id):
    """
    Vista detallada con la informacion de un usuario
    """
    usuario = board.get_usuario(id)
    form = ModificarUsuarioForm()
    form.set_from_usuarios(usuario)
    roles = board.get_roles()
    return render_template(
        "usuarios/usuario.html", usuario=usuario, form=form, roles=roles
    )


@usuario_blueprint.post("/<int:id>")
@login_required
@user_update_req
def update_usuario(id):
    """
    #Actualiza los datos de un usuario. Se necesita chequear que no se repita email ni username
    """
    usuario = board.get_usuario(id)
    form = ModificarUsuarioForm(request.form)
    if not form.validate:
        flash("No se pudo modificar al usuario", "danger")
        return redirect(url_for("usuarios.view_usuario", id=id))
    # Comprobar si se modificó el email
    if form.email.data != usuario.email:
        # Si se modificó, comprobar que el nuevo email no esté en uso
        if board.exist_email(form.email.data):
            flash("el email ingresado ya esta registrado", "danger")
            return redirect(url_for("usuarios.view_usuario", id=id))

    # Comprobar si se modificó el username
    if form.username.data != usuario.username:
        # Si se modificó, comprobar que el nuevo username no esté en uso
        if board.exist_username(form.username.data):
            flash("el username ingresado ya está registrado", "danger")
            return redirect(url_for("usuarios.view_usuario", id=id))

    # Validar email
    if not validate_email(form.email.data):
        flash("Ingrese un email con un formato válido", "danger")
        return redirect(url_for("usuarios.view_usuario", id=id))

    # Validar nombre, apellido y username
    if not validate_only_letters(form.username.data):
        flash("el nombre de usuario solo debe contener letras", "danger")
        return redirect(url_for("usuarios.view_usuario", id=id))
    if not validate_only_letters(form.first_name.data):
        flash("el nombre solo debe contener letras", "danger")
        return redirect(url_for("usuarios.view_usuario", id=id))
    if not validate_only_letters(form.last_name.data):
        flash("el apellido solo debe contener letras", "danger")
        return redirect(url_for("usuarios.view_usuario", id=id))
    

    # Si no están en uso el email nuevo ni el username nuevo actualiza los datos en la BD
    kwargs = {
        "id": id,
        "email": form.email.data,
        "username": form.username.data,
        "updated_at": datetime.now(),
        "first_name": form.first_name.data,
        "last_name": form.last_name.data,
    }
    board.update_usuario(**kwargs)
    flash("Se actualizaron los datos del usuario", "success")
    return redirect(url_for("usuarios.usuario_index"))

@usuario_blueprint.post("/modifyActivo/<int:id>")
@login_required
@user_update_req
def modify_activo(id):
    """
    Cambia el estado "activo" a su inverso.
    No se puede dar de baja a un administrador
    Si se inactiva a un usuario con perfil de socio, eliminar socio
    Si se activa a un usuario con perfil de socio, activar su perfil de socio
    """
    # Chequear que el usuario no sea administrador
    usuario = board.get_usuario(id)
    if board.usuario_has_rol("Administrador",usuario.id):
        flash("No se puede inactivar a un administrador", "danger")
        return redirect(url_for('usuarios.usuario_index'))

    # Chequear si se inactiva, a un usuario socio activo > inactivar socio
    if usuario.activo:
        socio = board.find_socio_by_id_usuario(id)
        if socio:
            if socio.activo:
                board.update_activo_usuario(id)
                board.soft_delete_socio(socio.id)
                flash("Se actualizo el estado del usuario, y el socio fue eliminado", "success")
                return redirect(url_for('usuarios.usuario_index'))

    # Chequear si: se activa a un usuario socio > activar socio
    if not usuario.activo:
        socio = board.find_socio_by_id_usuario(id)
        if socio:
            if not socio.activo:
                board.update_activo_usuario(id)
                kwargs = {
                    "activo": True,
                }
                board.update_socio(socio.id, **kwargs)
                flash("Se actualizo el estado del usuario, y el socio fue activado", "success")
                return redirect(url_for('usuarios.usuario_index'))

    
    # Cambiar estado usuario
    board.update_activo_usuario(id)
    flash("Se actualizo el estado del usuario", "success")
    return redirect(url_for('usuarios.usuario_index'))


@usuario_blueprint.post("/quitarRol")
@login_required
@user_rol_update_req
def quitar_rol():
    """
    Quitar un rol a un usuario.
    Si se quita el rol de socio se debe eliminar al socio
    """
    rol_id = request.form.get("rol_id")
    usuario_id = request.form.get("usuario_id")
    board.quitar_rol(rol_id, usuario_id)

    # Chequear si el rol es Socio
    rol_socio = board.get_rol_socio()
    if rol_socio.id == int(rol_id):
        # Si el usuario tiene perfil de socio y es un socio activo, borrarlo
        socio = board.find_socio_by_id_usuario(usuario_id)
        if socio:
            if socio.activo:
                board.soft_delete_socio(socio.id)
                flash("Se quitó el rol exitosamente, y el socio fue eliminado", "success")
                return redirect(url_for('usuarios.view_usuario',id=usuario_id))

    flash("Se quitó el rol exitosamente", "success")
    return redirect(url_for("usuarios.view_usuario", id=usuario_id))


@usuario_blueprint.post("/asignarRol")
@login_required
@user_rol_update_req
def asignar_rol():
    """
    Asignar un rol a un usuario
    Si el rol es 'Socio' se lo debe enviar a crear perfil de socio
    """    
    rol_id = request.form.get("rol_id")
    usuario_id = request.form.get("usuario_id")

    # Chequear si el rol es Socio
    rol_socio = board.get_rol_socio()
    if rol_socio.id == int(rol_id):
        # Si tiene perfil de socio, se le activa el perfil
        socio = board.find_socio_by_id_usuario(usuario_id)
        if socio:
            if not socio.activo:
                kwargs = {
                    "activo": True,
                }
                board.update_socio(socio.id, **kwargs)
        # Si no tiene perfil de socio, debe crearse uno
        else:
            return redirect(url_for('socios.add_socio', usuario_id=usuario_id))
    
    # Asignar el rol
    board.asignar_rol(rol_id, usuario_id)
    flash("Se asignó el rol al usuario", "success")
    return redirect(url_for('usuarios.view_usuario',id=usuario_id))


def validate_only_letters(string):
    """
    Verifica que el string solo contenga letras
    """
    valid_chars = " qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNMÁÉÚÍÓáéíóú"
    for char in string:
        if char not in valid_chars:
            return False
    return True


def validate_email(email):
    """
    verifica que el email ingresado tenga un formato valido
    """
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, email) is not None