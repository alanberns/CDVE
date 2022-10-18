from src.core import board
from dateutil.parser import parse



def run():
    """
    Crea datos por defecto para la base de datos
    """

    test_user = board.create_usuario(
        username="test",
        mail="test@test.com",
        contraseña="1234"
    )
    test_user2 = board.create_usuario(
        username="test2",
        mail="test2@test2.com",
        contraseña="1234"
    )
    # Configuracion
    default_config = board.init_configuracion(
        elementos_pagina=20,
        estado_pago=True,
        estado_info_contactos=True,
        texto_recibo="La cuota XXX ha sido pagada",
        valor_base_cuota=1000,
        porcentaje_cuota=0.15,
    )

    ###Roles
    rol_administrador = board.create_rol(nombre="administrador")

    ###Permisos
    permiso_index = board.create_permiso(nombre="index")
    permiso_show = board.create_permiso(nombre="show")
    board.rol_assign_permiso(rol_administrador, [permiso_index, permiso_show])

    socio1 = board.create_socio(
        id_usuario=1,
        # el id de usuario debería obtenerse desde el usuario
        tipo_documento="DNI",
        numero_documento=44556677,
        genero="femenino",
        numero_socio="AAA111",
        direccion="calle falsa 123",
        telefono=14141414,
        email="socio1@mail.com"
        # el usuario tiene mail también, arreglar.
    )

    juan = board.create_socio(
        id_usuario=2,
        # el id de usuario debería obtenerse desde el usuario
        tipo_documento="DNI",
        numero_documento=43123123,
        genero="caballo",
        numero_socio="AAA12",
        direccion="7 y 32",
        telefono=221420,
        email="juan@juan.juan"
        # el usuario tiene mail también, arreglar.
    )

    # Roles
    rol_administrador = board.create_rol(
        nombre="administrador"
    )

    # Permisos
    permiso_index = board.create_permiso(
        nombre="index"
    )
    permiso_show = board.create_permiso(
        nombre="show"
    )
    board.rol_assign_permiso(rol_administrador, [permiso_index, permiso_show])

    # Disciplinas
    t_disciplina = board.create_disciplina(
        id="1",
        nombre="Futbol",
    )

    t_disciplina2 = board.create_disciplina(
        id="3",
        nombre="Bascket",
    )

    t_disciplina3 = board.create_disciplina(
        id="7",
        nombre="Bascket",
    )

    cuota_enero = board.create_cuota(
        estado_pago=0,
        fecha_vencimiento=parse('2022-01-30 22:00:00'),
        fecha_pago=parse('2022-03-15 22:00:00'),
        valor_cuota=500,
        valor_pago=500,
        activo=True
    )

    cuota_febrero = board.create_cuota(
        estado_pago=0,
        fecha_vencimiento=parse('2022-02-28 22:00:00'),
        fecha_pago=parse('2022-03-15 20:00:00'),
        valor_cuota=520,
        valor_pago=520,
        activo=True
    )

    cuota_marzo = board.create_cuota(
        estado_pago=0,
        fecha_vencimiento=parse('2022-03-30 22:00:00'),
        fecha_pago=parse('2022-03-15 22:00:00'),
        valor_cuota=550,
        valor_pago=550,
        activo=True
    )

    board.socio_assign_disciplina(socio1, t_disciplina)
