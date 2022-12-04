from src.core.database import db
from src.core.board.usuario import Usuario
from src.core.board.configuracion import Configuracion
from src.core.board.rol import Rol
from src.core.board.permiso import Permiso
from src.core.board.disciplina import Disciplina
from src.core.board.socio import Socio
from src.core.board.carnet import Carnet
from src.core.board.cuota import Cuota
from src.core.board.pago import Pago
from src.core.board.inscripcion import Inscripcion
from src.core.board.usuario_tiene_rol import Usuario_tiene_rol
from datetime import datetime
from dateutil.relativedelta import relativedelta
from sqlalchemy import func


# Lista todas las disciplinas
def list_disciplinas_paginadas(page=1, per_page=10):
    return Disciplina.query.order_by(Disciplina.id.asc()).paginate(page=page, per_page=per_page, error_out=False)


def listAll_disciplinas():
    return Disciplina.query.all()


@classmethod
def get_disciplinas(self):
    disciplinas = Disciplina.query.all()
    for row in disciplinas:
        disciplina = Disciplina(row[1], row[2], row[3])
        disciplinas.append(disciplina)
    return disciplinas


# Busca una disciplina por su ID y la devuelve
def get_disciplina(id):
    disciplina = Disciplina.query.filter(Disciplina.id == id).first()
    return disciplina

# Cambia es estado de una disciplina


def update_estado_disciplina(id):
    disciplina = get_disciplina(id)
    disciplina.estado = not (disciplina.estado)
    db.session.commit()
    return disciplina

# Actualiza la informacion de una Disciplina


def update_disciplina(id, **kwargs):
    disciplina = get_disciplina(id)
    disciplina.update(**kwargs)
    db.session.commit()
    return disciplina


def record_update(record):
    db.session.add(record)
    db.session.commit()


def list_usuarios(page=1, per_page=10):
    """
    Lista los datos de los usuarios.
    """
    return Usuario.query.order_by(Usuario.last_name.asc()).paginate(page=page, per_page=per_page, error_out=False)


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
    usuario = Usuario.query.filter(Usuario.id == id).first()
    return usuario


def update_usuario(**kwargs):
    """
    Actualiza la informacion del usuario
    """
    usuario = get_usuario(kwargs["id"])
    usuario.update(**kwargs)
    db.session.commit()

    return usuario


def update_password(**kwargs):
    """
    Actualizar contraseña
    """
    usuario = get_usuario(kwargs["id"])
    usuario.update_password(kwargs["password"])
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
    return db.session.query(Usuario).filter(func.lower(Usuario.email) == func.lower(email)).first() != None


def exist_username(username):
    """
    Verifica que un username existe en la BD
    """
    return db.session.query(Usuario).filter(func.lower(Usuario.username) == func.lower(username)).first() != None


def filter_usuarios(email, activo, page=1, per_page=10):
    """
    Filtra a usuarios por email y estado. Si el email ingresado es vacio y el estado que se pide es ambos
    no se incluye en el filtrado.
    """
    if (email == ""):
        if (activo == ""):
            usuarios = Usuario.query.order_by(Usuario.last_name.asc()).paginate(
                page=page, per_page=per_page, error_out=False)
        else:
            usuarios = Usuario.query.filter_by(activo=activo).order_by(
                Usuario.last_name.asc()).paginate(page=page, per_page=per_page, error_out=False)
    else:
        if (activo != ""):
            usuarios = Usuario.query.filter(Usuario.activo == activo, Usuario.email.ilike(email + "%")).order_by(
                Usuario.last_name.asc()).paginate(page=page, per_page=per_page, error_out=False)
        else:
            usuarios = Usuario.query.filter(Usuario.email.ilike(email + "%")).order_by(
                Usuario.last_name.asc()).paginate(page=page, per_page=per_page, error_out=False)
    return usuarios


def quitar_rol(rol_id, usuario_id):
    """
    Elimina una tupla de 'usuario_tiene_rol', quita un rol a un usuario
    """
    usuario_tiene_rol = Usuario_tiene_rol.query.filter_by(
        usuario_id=usuario_id, rol_id=rol_id
    ).first()
    db.session.delete(usuario_tiene_rol)
    db.session.commit()


def asignar_rol(rol_id, usuario_id):
    """
    Asigna un rol a un usuario
    """
    usuario = get_usuario(usuario_id)
    rol = Rol.query.filter(Rol.id == rol_id).first()
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


def get_rol_socio():
    """
    Retorna el rol socio
    """
    roles = get_roles()
    for rol in roles:
        if rol.nombre == "Socio":
            return rol


def usuario_has_rol(rol_name, usuario_id):
    """
    Indica si el rol esta asignado al usuario
    """
    usuario = get_usuario(usuario_id)
    for rol in usuario.roles:
        if rol.nombre == rol_name:
            return True
    return False


def find_user_by_email(email):
    """
    Devuelve un usuario dado un mail.
    """
    usuario = Usuario.query.filter_by(email=email).first()
    return usuario


def list_configuracion():
    """
    Lista los datos de la configuracion, devuelve una sola tupla
    """
    return Configuracion.query.first()


def list_disciplinas_activas(page):
    """
    Retorna las disciplinas activas
    """
    per_page = get_elements_per_page()
    return Disciplina.query.filter_by(estado=True).paginate(page=page, per_page=per_page)


def list_all_disciplinas_activas():
    """
    Retorna las disciplinas activas
    """
    return Disciplina.query.filter_by(estado=True).all()


def get_disciplinas_time(hora):
    """
    retorna las disciplinas que comienzan a la hora indicada
    """
    return Disciplina.query.filter(Disciplina.hora.ilike(hora + "%")).all()


def get_disciplinas_by_user_id(socio_id):
    """
    Retorna las disciplinas dado el id de un socio
    """
    return Disciplina.query.join(Inscripcion).join(Socio).filter(
        Disciplina.estado == True,
        Socio.id == socio_id
    )


def list_disciplinas():
    return Disciplina.query.all()


def list_disciplinas_not_socio(socio_id):
    disciplinas_inscripto = db.session.query(Inscripcion.disciplina_id).filter(
        Inscripcion.socio_id == socio_id
    )
    return Disciplina.query.filter(
        ~Disciplina.id.in_(
            disciplinas_inscripto), Disciplina.estado == True
    ).all()


def find_disciplina_by_id(disciplina_id):
    disciplina = Disciplina.query.filter_by(id=disciplina_id).first()
    return disciplina


def find_disciplina_by_name(disciplina_name):
    disciplina = Disciplina.query.filter(
        Disciplina.nombre.ilike(f"{disciplina_name}%")).first()
    return disciplina


def delete_disciplina(id):
    disciplina = Disciplina.query.get(id)
    disciplina.estado = ("Inactivo",)
    db.session.commit()


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
    """
    Crea un Socio y lo agrega la db"
    """
    socio = Socio(**kwargs)
    db.session.add(socio)
    db.session.commit()
    return socio


def list_socios():
    """
    Devuelve la lista de socios activos (sin borrado lógico)
    """
    socios = (
        db.session.query(Socio, Usuario)
        .filter_by(activo=True)
        .outerjoin(Usuario, full=True)
        .all()
    )
    return socios


def list_socios_all():
    """
    Devuelve todos los socios activos
    """
    return Socio.query.filter_by(activo=True).all()


def find_socio_by_id_usuario(usuario_id):
    """
    Devuelve un socio por el id de usuario
    """
    socio = db.session.query(Socio, Usuario).outerjoin(
        Usuario, full=True).filter_by(id=usuario_id).first()
    return socio[0]


def list_socios_join_users(page=1, per_page=10):
    """
    Devuelve la lista de socios activos (sin borrado lógico)
    """
    socios = (
        db.session.query(Socio, Usuario, Carnet)
        .filter_by(activo=True)
        .outerjoin(Usuario, full=True)
        .order_by(Usuario.last_name)
        .outerjoin(Carnet, full=True)
        .paginate(page=page, per_page=per_page, error_out=False)
    )
    return socios


def list_socios_habilitado(habilitado, page=1, per_page=10):
    """
    Devuelve la lista de socios activos habilitados o deshabilitados
    """
    socios = (
        db.session.query(Socio, Usuario, Carnet)
        .filter_by(activo=True, habilitado=habilitado)
        .outerjoin(Usuario, full=True)
        .order_by(Usuario.last_name)
        .outerjoin(Carnet, full=True)
        .paginate(page=page, per_page=per_page, error_out=False)
    )
    return socios


def find_socio_by_apellido(last_name, page=1, per_page=10):
    """
    Devuelve los socios activos dado un apellido
    """
    socios = (
        db.session.query(Socio, Usuario, Carnet)
        .filter_by(activo=True)
        .outerjoin(Usuario, full=True)
        .filter(Usuario.last_name.ilike(f"{last_name}%"))
        .order_by(Usuario.last_name)
        .outerjoin(Carnet, full=True)
        .paginate(page=page, per_page=per_page, error_out=False)
    )
    return socios


def find_socio_habilitado_by_apellido(last_name, habilitado, page=1, per_page=10):
    """
    Devuelve una lista de socios activos dado un apellido y un estado de "habilitado".
    """
    socios = (
        db.session.query(Socio, Usuario, Carnet)
        .filter_by(activo=True, habilitado=habilitado)
        .outerjoin(Usuario, full=True)
        .filter(Usuario.last_name.ilike(f"{last_name}%"))
        .order_by(Usuario.last_name)
        .outerjoin(Carnet, full=True)
        .paginate(page=page, per_page=per_page, error_out=False)
    )
    return socios


def find_socio_by_id(socio_id):
    """
    Devuelve un socio dado un id.
    """
    socio = Socio.query.filter_by(id=socio_id).first()
    return socio


def find_socio_join_usuario_by_id(socio_id):
    """
    Devuelve la información de un socio junto con su información de usuario.
    """
    socio = (
        db.session.query(Socio, Usuario)
        .filter_by(activo=True, id=socio_id)
        .outerjoin(Usuario, full=True)
        .first()
    )
    return socio


def exist_socio_documento(documento):
    """
    Verifica que el documento dado está disponible y no le pertenece a otro socio activo
    """
    return (
        Socio.query.filter(
            Socio.numero_documento == documento, Socio.activo == True
        ).first()
        == None
    )


def exist_socio_documento_id(documento, id):
    """
    Verifica que existe un socio con un documento dado y sólo pertenece al ingresado
    """
    return (
        Socio.query.filter(Socio.numero_documento ==
                           documento, Socio.id != id).first()
        == None
    )


def update_socio(socio_id, **kwargs):
    """
    Actualiza la información de un socio dado un id.
    """
    socio = find_socio_by_id(socio_id)
    socio.update(**kwargs)
    db.session.merge(socio)
    db.session.commit()

    return socio


def soft_delete_socio(socio_id):
    """
    Realiza la baja lógica de un socio dado un id.
    """
    socio = find_socio_by_id(socio_id)
    socio.activo = False
    db.session.merge(socio)
    db.session.commit()

    return socio


def switch_state_socio(socio_id):
    """
    Cambia el estado del campo "habilitado" de un socio dado un id.
    """
    socio = find_socio_by_id(socio_id)
    socio.habilitado = not socio.habilitado
    db.session.merge(socio)
    db.session.commit()

    return socio


def create_cuota(**kwargs):
    """
    Crea una cuota dados los argumentos correspondientes
    """
    cuota = Cuota(**kwargs)
    db.session.add(cuota)
    db.session.commit()
    return cuota


def socio_assign_disciplina(socio, disciplina):
    """
    Asigna una disciplina a un socio
    """
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


def get_inscripciones(page):
    """
    Retorna las Inscripciones
    """
    per_page = get_elements_per_page()
    return Inscripcion.query.join(Disciplina).filter(
        Disciplina.estado == True
    ).paginate(page=page, per_page=per_page)


def get_inscripcion_by_socio_and_disciplina(socio, disciplina):
    """
    Retorna una inscripcion, dado un socio y una disciplina
    """
    inscripcion = Inscripcion.query.filter_by(
        socio_id=socio.id, disciplina_id=disciplina.id
    ).join(Disciplina).filter(
        Disciplina.estado == True
    ).first()
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


def get_cuotas_adeudadas_by_inscripcion_id(inscripcion_id):
    """
    Retorna las cuotas para un socio dado su id
    """
    return Cuota.query.filter_by(inscripcion_id=inscripcion_id).filter_by(estado_pago=False).all()


def pay_cuotas_by_ids(cuota_ids):
    """
    Paga multiples cuotas, pasadas como una lista de ids de cuotas
    """
    cuotas = Cuota.query.filter(Cuota.id.in_(cuota_ids)).all()
    for cuota in cuotas:
        cuota.pagar()
        record_update(cuota)
    return cuotas


def get_cuotas_by_ids(cuota_ids):
    """
    Obtiene multiples cuotas, dada una lista de ids de cuotas
    """
    return Cuota.query.filter(Cuota.id.in_(cuota_ids)).all()


def get_cuotas_by_socio_id_and_nro_cuota(socio_id, nro_cuota, inscripcion):
    """
    Retorna las cuotas para un socio dado su id
    """
    cuota = Cuota.query.join(Inscripcion.cuota).filter(
        Inscripcion.socio_id == socio_id,
    ).filter(
        Cuota.nro_cuota == nro_cuota,
    ).first()
    return cuota


def user_get_permisos(usuario_id):
    """
    Obtiene los permisos dada la id de un usuario
    """
    roles = Rol.query.join(Usuario_tiene_rol).filter_by(
        usuario_id=usuario_id).all()
    permisos = list(
        {permiso.nombre for rol in roles for permiso in rol.permisos})
    return permisos


def get_pagos():
    """
    Retorna los pagos
    """
    return Pago.query.all()


def get_pago_by_id(pago_id):
    """
    Retorna los pagos dada una id de pago
    """
    return Pago.query.filter_by(id=pago_id).first()


def list_pagos(page):
    """
    Retorna los pagos
    """
    per_page = get_elements_per_page()
    return Pago.query.paginate(page=page, per_page=per_page)


def pago_assign_cuotas(pago, cuotas):
    """
    Agrega una lista de cuotas a una inscripcion
    """
    pago.cuotas.extend(cuotas)
    record_update(pago)
    return pago


def create_pago(**kwargs):
    """
    Crea un pago
    """
    pago = Pago(**kwargs)
    record_update(pago)
    return pago


def set_nro_cuota_by_inscripcion(inscripcion_id):
    """
    Setea los numeros de cuota para cuotas, que no tienen numero
    """
    cuotas = (
        Cuota.query.filter_by(inscripcion_id=inscripcion_id, nro_cuota=None)
        .order_by(Cuota.fecha_vencimiento.asc())
        .all()
    )
    for count, cuota in enumerate(cuotas, start=1):
        cuota.nro_cuota = count
        record_update(cuota)


def get_elements_per_page():
    """
    Obtiene la cantidad de elementos por pagina, seteados en la configuracion
    """
    config = list_configuracion()
    return config.elementos_pagina


def generate_payment(cuota_ids):
    """
    Realiza un pago dado una lista de ids de cuotas
    """
    time_stamp = datetime.now()
    cuotas = pay_cuotas_by_ids(cuota_ids)
    monto = sum(cuota.valor_cuota for cuota in cuotas)
    pago = create_pago(fecha=time_stamp, monto=monto)
    pago_assign_cuotas(pago, cuotas)
    return pago


def get_pagos_search_paginated(page, filter, search_text):
    """
    Retorna los pagos de forma paginada, filtrados segun la busqueda que haya hecho el usuario
    en la vista de pagos
    """
    per_page = get_elements_per_page()
    if filter == 1:
        return Pago.query.join(Cuota.pago).join(Inscripcion).join(Socio).join(Usuario).filter(Usuario.last_name.ilike(f"{search_text}%")).distinct().paginate(page=page, per_page=per_page)
    elif filter == 0:
        return (
            Pago.query.join(Cuota.pago)
            .join(Inscripcion)
            .join(Socio)
            .filter(Socio.id == search_text)
            .distinct()
            .paginate(page=page, per_page=per_page)
        )


def create_cuotas_by_inscripcion(socio, disciplina):
    """
    Crea las cuotas para una disciplina, se utiliza al momento de inscribir un usuario
    """
    valor_base = list_configuracion().valor_base_cuota
    cuotas = []
    for numero in range(1, 12):
        fecha_cuota = datetime.today() + relativedelta(months=numero)
        fecha = fecha_cuota.replace(day=10)
        cuota = create_cuota(
            nro_cuota=numero,
            estado_pago=0,
            fecha_vencimiento=fecha,
            valor_cuota=valor_base + disciplina.costo_mensual,
            activo=True,
        )
        cuotas.append(cuota)
    inscripion_assign_cuotas(socio, disciplina, cuotas)


def update_valor_cuotas(new_value_cuota):
    """
    Actualiza el valor de una cuota, segun el valor pasado por parametro. Se utiliza al cambiar el
    valor base de la cuota en la configuracion
    """
    fecha_actual = datetime.now()
    cuotas = Cuota.query.filter(
        Cuota.estado_pago == False, Cuota.fecha_vencimiento > fecha_actual
    ).all()
    for cuota in cuotas:
        cuota.valor_cuota = new_value_cuota + cuota.inscripcion.disciplina.costo_mensual
        record_update(cuota)
    return cuotas


def get_pagos_by_socio_id(socio_id, page):
    per_page = get_elements_per_page()
    return Pago.query.join(Cuota.pago).join(Inscripcion).join(Socio).filter(Socio.id == socio_id).distinct().paginate(page=page, per_page=per_page)


def get_cuota_by_inscripcion_id_and_nro_cuota(inscripcion_id, nro_cuota):
    return Cuota.query.filter_by(
        inscripcion_id=inscripcion_id,
        nro_cuota=nro_cuota
    ).join(Inscripcion).join(Disciplina).filter(
        Disciplina.estado == True
    ).first()


def create_carnet(**kwargs):
    """
    Crea un carnet y lo agrega en la BD.
    """
    carnet = Carnet(**kwargs)
    db.session.add(carnet)
    db.session.commit()
    return carnet


def get_carnet(socio_id):
    """
    Devuelve un carnet según un id de socio.
    """
    carnet = Carnet.query.filter(Carnet.id_socio == socio_id).first()
    return carnet


def es_moroso(socio_id):
    """
    Devuelve un boolean indicando si el socio dado es moroso.
    """
    cuotas = Cuota.query.join(Inscripcion).filter(
        Inscripcion.socio_id == socio_id).all()
    for cuota in cuotas:
        print(cuota.id)
        if (cuota.fecha_vencimiento < datetime.today() and (not cuota.estado_pago)):
            return True
    return False

def delete_carnet(socio_id):
    """
    Elimina el carnet de un socio.
    """
    db.session.query(Carnet).filter(Carnet.id_socio == socio_id).delete()
    db.session.commit()

def set_comprobante_by_pago_id(pago_id, filename):
    """
    Dada una id de pago y un nombre de archivo, guarda el nombre del arcivo guardado,
    el cual se ubicara por defector en la carpeta public/comprobantes
    """
    pago = get_pago_by_id(pago_id)
    pago.comprobante = filename
    record_update(pago)
    return pago
