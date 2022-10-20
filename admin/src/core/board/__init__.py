from src.core.database import db
from src.core.board.usuario import Usuario
from src.core.board.configuracion import Configuracion
from src.core.board.rol import Rol
from src.core.board.permiso import Permiso
from src.core.board.disciplina import Disciplina
from src.core.board.socio import Socio
from src.core.board.cuota import Cuota
from src.core.board.inscripcion import Inscripcion
from src.core.board.usuario_tiene_rol import Usuario_tiene_rol


def list_usuarios(page=1, per_page=10):
    """
    Lista los datos de los usuarios.
    """
    return Usuario.query.order_by(Usuario.id.asc()).paginate(page=page, per_page=per_page, error_out=False)


def create_usuario(**kwargs):
    """
    Crea un usuario y lo agrega en la BD. Devuelve el usuario creado.
    No se puede repetir: Email ni username.
    """
    usuario = Usuario(**kwargs)
    db.session.add(usuario)
    db.session.commit()
    return usuario


def get_usuario(id):
    """
    Busca un usuario por su id y lo devuelve
    """
    usuario = db.session.get(Usuario, id)
    return usuario


def update_usuario(**kwargs):
    """
    Actualiza la informacion del usuario
    """
    usuario = get_usuario(kwargs['id'])
    usuario.update(**kwargs)
    db.session.commit()

    return usuario


def update_activo_usuario(id):
    """
    Actualiza el estado (Activo) del usuario.
    """
    usuario = get_usuario(id)
    usuario.activo = not usuario.activo

    db.session.commit()

    return usuario


def exist_email(email):
    """
    Verifica que un email existe en la BD
    """
    return Usuario.query.filter(Usuario.email == email).first() != None


def exist_username(username):
    """
    Verifica que un username existe en la BD
    """
    return Usuario.query.filter(Usuario.username == username).first() != None


def filter_usuarios(email, activo, page=1, per_page=10):
    """
    Filtra a usuarios por email y estado. Si el email ingresado es vacio y el estado que se pide es ambos 
    no se incluye en el filtrado.
    """
    if (email == ""):
        if (activo == ""):
            usuarios = Usuario.query.order_by(Usuario.id.asc()).paginate(
                page=page, per_page=per_page, error_out=False)
        else:
            usuarios = Usuario.query.filter_by(activo=activo).order_by(
                Usuario.id.asc()).paginate(page=page, per_page=per_page, error_out=False)
    else:
        if (activo != ""):
            usuarios = Usuario.query.filter_by(activo=activo, email=email).order_by(
                Usuario.id.asc()).paginate(page=page, per_page=per_page, error_out=False)
        else:
            usuarios = Usuario.query.filter_by(email=email).order_by(
                Usuario.id.asc()).paginate(page=page, per_page=per_page, error_out=False)
    return usuarios


def quitar_rol(rol_id, usuario_id):
    """
    Elimina una tupla de 'usuario_tiene_rol', quita un rol a un usuario
    """
    usuario_tiene_rol = Usuario_tiene_rol.query.filter_by(
        usuario_id=usuario_id, rol_id=rol_id).first()
    db.session.delete(usuario_tiene_rol)
    db.session.commit()


def asignar_rol(rol_id, usuario_id):
    """
    Asigna un rol a un usuario
    """
    usuario = get_usuario(usuario_id)
    rol = db.session.get(Rol, rol_id)
    rol_list = []
    rol_list.append(rol)
    usuario.roles.extend(rol_list)
    db.session.add(usuario)
    db.session.commit()


def get_roles():
    """
    Retorna los roles
    """
    return Rol.query.all()


def find_user_by_email(email):
    usuario = Usuario.query.filter_by(email=email).first()
    return usuario


def list_configuracion():
    """
    Lista los datos de la configuracion, devuelve una sola tupla
    """

    return Configuracion.query.all()


def init_configuracion(**kwargs):
    """
    Crea los valores iniciales para la configuracion
    """
    configuracion = Configuracion(**kwargs)
    db.session.add(configuracion)
    db.session.commit()

    return configuracion


def update_configuracion(**kwargs):
    """
    Actualiza los datos de la configuracion
    """
    configuracion = Configuracion.query.first()
    configuracion.update(**kwargs)
    db.session.merge(configuracion)
    db.session.commit()

    return configuracion


def create_rol(**kwargs):
    """
    Crea un rol y lo agrega a la bd
    """
    rol = Rol(**kwargs)
    db.session.add(rol)
    db.session.commit()

    return rol


def create_permiso(**kwargs):
    """
    Crea un permiso y lo agrega a la bd
    """
    permiso = Permiso(**kwargs)
    db.session.add(permiso)
    db.session.commit()

    return permiso


def rol_assign_permiso(rol, permisos):
    """
    A un rol le asigna un permiso, agregando ambos a la tabla intermedia rol_tiene_permiso
    """
    rol.permisos.extend(permisos)
    db.session.add(rol)
    db.session.commit()
    return rol


def create_disciplina(**kwargs):
    """
    Crea una Disciplina y lo agrega la db"
    """

    disciplina = Disciplina(**kwargs)
    db.session.add(disciplina)
    db.session.commit()
    return disciplina


def create_socio(**kwargs):
    socio = Socio(**kwargs)
    db.session.add(socio)
    db.session.commit()
    return socio


def list_socios():
    socios = Socio.query.filter_by(activo=True).all()
    return socios


def list_socios_habilitado(habilitado):
    socios = Socio.query.filter_by(activo=True, habilitado=habilitado).all()
    return socios


def find_socio_by_apellido(username):
    socio = Socio.query.filter_by(activo=True).join(
        Usuario).filter_by(username=username).all()
    return socio


def find_socio_habilitado_by_apellido(username, habilitado):
    socio = Socio.query.filter_by(activo=True, habilitado=habilitado).join(
        Usuario).filter_by(username=username).all()
    # reemplazar "username" por apellido cuando haya
    return socio


def find_socio_by_id(socio_id):
    socio = Socio.query.filter_by(id=socio_id).first()
    return socio


def update_socio(socio_id, **kwargs):

    socio = find_socio_by_id(socio_id)
    socio.update(**kwargs)
    db.session.merge(socio)
    db.session.commit()

    return socio


def soft_delete_socio(socio_id):
    socio = find_socio_by_id(socio_id)
    socio.activo = False
    db.session.merge(socio)
    db.session.commit()

    return socio


def switch_state_socio(socio_id):
    socio = find_socio_by_id(socio_id)
    socio.habilitado = not socio.habilitado
    db.session.merge(socio)
    db.session.commit()

    return socio


def create_cuota(**kwargs):
    cuota = Cuota(**kwargs)
    db.session.add(cuota)
    db.session.commit()
    return cuota


def socio_assign_disciplina(socio, disciplina):
    inscripcion = Inscripcion()
    inscripcion.disciplina = disciplina
    socio.disciplina.append(inscripcion)
    db.session.add(socio)
    db.session.commit()
    return socio


def get_elementos_pagina():
    """
    Devuelve los elementos por pagina seteados en la configuracion
    """
    configuracion = Configuracion.query.first()

    return configuracion.elementos_pagina


def get_inscripciones():
    """
    Retorna las Inscripciones
    """
    return Inscripcion.query.all()


def get_inscripcion_by_socio_and_disciplina(socio, disciplina):
    """
    Retorna una inscripcion, dado un socio y una disciplina
    """
    inscripcion = Inscripcion.query.filter_by(
        socio_id=socio.id, disciplina_id=disciplina.id).first()
    return inscripcion


def inscripion_assign_cuotas(socio, disciplina, cuotas):
    """
    Agrega una lista de cuotas a una inscripcion
    """
    inscripcion = get_inscripcion_by_socio_and_disciplina(socio, disciplina)
    inscripcion.cuota.extend(cuotas)
    db.session.add(inscripcion)
    db.session.commit()
    return inscripcion


def get_cuotas_by_inscripcion_id(inscripcion_id):
    """
    Retorna las cuotas para un socio dado su id
    """
    return Cuota.query.filter_by(inscripcion_id=inscripcion_id).all()


def pagar_cuota_by_id(id_cuota):
    cuota = Cuota.query.filter_by(id=id_cuota).first()
    cuota.estado_pago = True
    db.session.add(cuota)
    db.session.commit()
    return cuota
