from flask import Blueprint
from flask import render_template
from flask import request
from pathlib import Path
from flask import redirect
from flask import url_for
from flask import flash
from datetime import datetime

from src.core import board


usuario_blueprint = Blueprint(
    "usuarios", __name__, url_prefix="/usuarios")




@usuario_blueprint.get("/")
def usuario_index():
    """
    Menu inicial de usuarios: lista de usuarios
    """
    configuracion = board.list_configuracion()
    elementos_pagina = configuracion[0].elementos_pagina
    page = int(request.args.get('page', 1))
    usuarios_pag = board.list_usuarios(page,elementos_pagina)
    return render_template("usuarios/usuarios.html", usuarios_pag=usuarios_pag)

@usuario_blueprint.get("/res")
def busqueda_filtrada():
    """
    Filtrar usuarios por email y estado.
    """
    configuracion = board.list_configuracion()
    elementos_pagina = configuracion[0].elementos_pagina
    email = ""
    if (request.args.get("email") != ""):
        email = request.args.get("email")
    if (request.args.get("estado") == "activo"):
        activo = True 
    else:
        if (request.args.get("estado") == "inactivo"):
            activo = False
        else:
            activo = ""
    page = int(request.args.get('page', 1))
    usuarios_pag = board.filter_usuarios(email, activo, page, elementos_pagina)
    return render_template("usuarios/usuariosFilter.html", 
    usuarios_pag=usuarios_pag, email=email, activo=request.args.get("estado"))

@usuario_blueprint.get("/add")
def add_usuario_view():
    """
    Vista para añadir un usuario
    """
    return render_template("usuarios/nuevoUsuario.html")

@usuario_blueprint.post("/add")
def add_usuario():
    """
    Añadir usuario. Se necesita chequear que no se repita email ni username. Vuelve a menu usuarios
    """
    if (board.exist_email(request.form.get("email"))):
        flash("El email ingresado ya está registrado", "danger")
        return redirect(url_for('usuarios.add_usuario_view'))
    if (board.exist_username(request.form.get("username"))):
        flash("El username ingresado ya está registrado", "danger")
        return redirect(url_for('usuarios.add_usuario_view'))

    board.create_usuario(
        username = request.form.get("username"),
        email = request.form.get("email"),
        password = request.form.get("password"),
        activo = True,
        created_at = datetime.now(),
        updated_at = datetime.now(),
        first_name = request.form.get("first_name"),
        last_name = request.form.get("last_name"),
        )
    flash("Se creó el nuevo usuario", "success")
    return redirect(url_for('usuarios.usuario_index'))

@usuario_blueprint.get("/<int:id>")
def view_usuario(id):
    """
    Vista detallada con la informacion de un usuario
    """
    usuario = board.get_usuario(id)
    roles = board.get_roles()
    return render_template("usuarios/usuario.html", usuario=usuario, roles=roles)

@usuario_blueprint.post("/<int:id>")
def update_usuario(id):
    """
    #Actualiza los datos de un usuario. Se necesita chequear que no se repita email ni username
    """
    usuario = board.get_usuario(id)
    #Comprobar si se modificó el email
    if (request.form.get("email") != usuario.email):
        #Si se modificó, comprobar que el nuevo email no esté en uso
        if (board.exist_email(request.form.get("email"))):
            flash("el email ingresado ya esta registrado", "danger")
            return redirect(url_for('usuarios.view_usuario', id=id))

    #Comprobar si se modificó el username
    if (request.form.get("username") != usuario.username):
        #Si se modificó, comprobar que el nuevo username no esté en uso
        if (board.exist_username(request.form.get("username"))):
            flash("el username ingresado ya está registrado", "danger")
            return redirect(url_for('usuarios.view_usuario', id=id))
    
    #Si no están en uso el email nuevo ni el username nuevo actualiza los datos en la BD
    kwargs = {
            "id": id,
            "email": request.form.get("email"),
            "username": request.form.get("username"),
            "updated_at": datetime.now(),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
        }
    board.update_usuario(**kwargs)
    flash("Se actualizaron los datos del usuario", "success")
    return redirect(url_for('usuarios.usuario_index'))

@usuario_blueprint.get("/modifyActivo/<int:id>")
def modify_activo(id):
    """
    Cambia el estado de activo a su inverso.
    No se puede dar de baja a un administrador
    """
    board.update_activo_usuario(id)
    flash("Se actualizo el estado del usuario", "success")
    return redirect(url_for('usuarios.usuario_index', id=id))

@usuario_blueprint.post("/")
def delete_usuario():
    """
    Recibe el id de un usuario para eliminarlo de la BD
    """
    board.delete_usuario(request.form.get("id"))
    flash("Se eliminó al usuario", "success")
    return (redirect(url_for('usuarios.usuario_index')))

@usuario_blueprint.get("/quitarRol")
def quitar_rol():
    """
    Quitar un rol a un usuario
    """
    rol_id = request.args.get("rol_id")
    usuario_id = request.args.get("usuario_id")
    board.quitar_rol(rol_id, usuario_id)
    flash("Se quitó el rol exitosamente", "success")
    return redirect(url_for('usuarios.view_usuario',id=usuario_id))


@usuario_blueprint.get("/asignarRol")
def asignar_rol():
    """
    Asignar un rol a un usuario
    """
    rol_id = request.args.get("rol_id")
    usuario_id = request.args.get("usuario_id")
    board.asignar_rol(rol_id, usuario_id)
    flash("Se asignó el rol al usuario", "success")
    return redirect(url_for('usuarios.view_usuario',id=usuario_id))
