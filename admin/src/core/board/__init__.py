from src.core.database import db
from src.core.board.usuario import Usuario
from src.core.board.configuracion import Configuracion
from src.core.board.rol import Rol
from src.core.board.permiso import Permiso
from src.core.board.socio import Socio


def list_usuarios():
    return Usuario.query.all()


def create_usuario(**kwargs):
    usuario = Usuario(**kwargs)
    db.session.add(usuario)
    db.session.commit()
    return usuario


def find_user_by_mail_and_pass(mail, contraseña):
    usuario = Usuario.query.filter_by(mail=mail, contraseña=contraseña).first()
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
    socio = Socio.query.filter_by(activo=True).join(Usuario).filter_by(username=username).all() 
    return socio

def find_socio_habilitado_by_apellido(username, habilitado):
    socio = Socio.query.filter_by(activo=True, habilitado=habilitado).join(Usuario).filter_by(username=username).all() 
    #reemplazar "username" por apellido cuando haya
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