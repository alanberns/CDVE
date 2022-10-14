from src.core.database import db
from src.core.board.usuario import Usuario
from src.core.board.configuracion import Configuracion
from src.core.board.rol import Rol
from src.core.board.permiso import Permiso

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
    usuario.username = kwargs['username']
    usuario.email = kwargs['email']
    usuario.last_name = kwargs['last_name']
    usuario.first_name = kwargs['first_name']
    usuario.updated_at = kwargs['updated_at']

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

def delete_usuario(id):
    """
    Elimina el usuario de la BD
    """
    db.session.delete(get_usuario(id))
    db.session.commit()

def filter_usuarios(email, activo, page=1, per_page=10):
    """
    Filtra a usuarios por email y estado. Si el email ingresado es vacio y el estado que se pide es ambos 
    no se incluye en el filtrado.
    """
    if (email == ""):
        if (activo == ""):
            usuarios = Usuario.query.order_by(Usuario.id.asc()).paginate(page=page, per_page=per_page, error_out=False)
        else: 
            usuarios = Usuario.query.filter_by(activo=activo).order_by(Usuario.id.asc()).paginate(page=page, per_page=per_page, error_out=False)
    else:
        if (activo != ""):
            usuarios = Usuario.query.filter_by(activo=activo, email=email).order_by(Usuario.id.asc()).paginate(page=page, per_page=per_page, error_out=False)
        else:
            usuarios = Usuario.query.filter_by(email=email).order_by(Usuario.id.asc()).paginate(page=page, per_page=per_page, error_out=False)
    return usuarios

def find_user_by_mail_and_pass(mail,contraseña):
    usuario = Usuario.query.filter_by(mail=mail, contraseña = contraseña).first()
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

def rol_assign_permiso(rol,permisos):
    """
    A un rol le asigna un permiso, agregando ambos a la tabla intermedia rol_tiene_permiso
    """
    rol.permisos.extend(permisos)
    db.session.add(rol)
    db.session.commit()
    return rol