from src.core import board
from dateutil.parser import parse
from datetime import datetime


def run():
    """
    Crea datos por defecto para la base de datos
    """

    # Usuarios
    test_user = board.create_usuario(
        username="test",
        email="test@test.com",
        password="12345",
        first_name="Aaa",
        last_name="Bbb",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    test_user2 = board.create_usuario(
        username="test2",
        email="test2@test2.com",
        password="12345",
        first_name="Ccc",
        last_name="Ddd",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    # Configuracion
    default_config = board.init_configuracion(
        elementos_pagina=20,
        estado_pago=True,
        estado_info_contactos=True,
        texto_recibo="Recibimos de USUARIO el importe en pesos de MONTO por el concepto de cuota societaria de la disciplina DISCIPLINA. A continuacion se detalla lo pagado.",
        valor_base_cuota=1000,
        porcentaje_cuota=0.15,
    )

    # Roles
    rol_administrador = board.create_rol(nombre="Administrador")
    rol_operador = board.create_rol(nombre="Operador")
    rol_usuario = board.create_rol(nombre="Socio")

    # Permiso Configuracion
    configuracion_all = board.create_permiso(nombre="configuracion_all")

    # Permisos Pagos
    pago_index = board.create_permiso(nombre="pago_index")
    pago_show = board.create_permiso(nombre="pago_show")
    pago_update = board.create_permiso(nombre="pago_update")
    pago_delete = board.create_permiso(nombre="pago_delete")
    board.rol_assign_permiso(rol_administrador, [
                             configuracion_all, pago_index, pago_show, pago_update, pago_delete])

    board.rol_assign_permiso(rol_operador, [
                             pago_index, pago_show, pago_update])

    # Permisos modulo usuarios
    user_index = board.create_permiso(nombre="user_index")
    user_create = board.create_permiso(nombre="user_create")
    user_delete = board.create_permiso(nombre="user_delete")
    user_update = board.create_permiso(nombre="user_update")
    user_show = board.create_permiso(nombre="user_show")
    user_rol_update = board.create_permiso(nombre="user_rol_update")
    board.rol_assign_permiso(rol_administrador, [user_index, user_create, user_show,
                                                 user_delete, user_rol_update, user_update])

    socio1 = board.create_socio(
        id_usuario=1,
        # el id de usuario debería obtenerse desde el usuario
        tipo_documento="DNI",
        numero_documento=44556677,
        genero="femenino",
        direccion="calle falsa 123",
        telefono=14141414,
        # el usuario tiene mail también, arreglar.
    )

    socio2 = board.create_socio(
        id_usuario=2,
        # el id de usuario debería obtenerse desde el usuario
        tipo_documento="DNI",
        numero_documento=43123123,
        genero="Masculino",
        direccion="7 y 32",
        telefono=221420,
        # el usuario tiene mail también, arreglar.
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
        nombre="Futbol",
        categoria="2010",
        entrenador="Carlos Bianchi",
        dia="Martes",
        hora="17 Hs",
        costo_mensual="5000",
        estado="Activo",
    )
    t_disciplina2 = board.create_disciplina(
        nombre="Tenis",
        categoria="Mini",
        entrenador="Sebastian Coria",
        dia="Miercoles",
        hora="16 Hs",
        costo_mensual="3000",
        estado="Activo",
    )
    t_disciplina3 = board.create_disciplina(
        nombre="Basquet",
        categoria="Sub 19 ",
        entrenador="Facundo Campazzo",
        dia="Viernes",
        hora="17 Hs",
        costo_mensual="4000",
        estado="Activo",
    )
    t_disciplina4 = board.create_disciplina(
        nombre="Tenis",
        categoria="2017 ",
        entrenador="Rafael Nadal",
        dia="Jueves",
        hora="13 Hs",
        costo_mensual="3400",
        estado="Activo",
    )
    t_disciplina5 = board.create_disciplina(
        nombre="Handball",
        categoria="2017 ",
        entrenador="Gonzalo Carou",
        dia="Viernes",
        hora="17 Hs",
        costo_mensual="3400",
        estado="Activo",
    )
    t_disciplina5 = board.create_disciplina(
        nombre="Hockey",
        categoria="Mini",
        entrenador="Maria Forcherio",
        dia="Viernes",
        hora="18 Hs",
        costo_mensual="4600",
        estado="Activo",
    )
    t_disciplina5 = board.create_disciplina(
        nombre="Futbol",
        categoria="2014 ",
        entrenador="Marcelo Gallardo",
        dia="Lunes",
        hora="14 Hs",
        costo_mensual="7600",
        estado="Activo",
    )

    cuota_enero = board.create_cuota(
        estado_pago=0,
        fecha_vencimiento=parse('2022-01-10 22:00:00'),
        valor_cuota=500,
        activo=True
    )

    cuota_febrero = board.create_cuota(
        estado_pago=0,
        fecha_vencimiento=parse('2022-02-10 22:00:00'),
        valor_cuota=520,
        activo=True
    )

    cuota_marzo = board.create_cuota(
        estado_pago=0,
        fecha_vencimiento=parse('2022-03-10 22:00:00'),
        valor_cuota=550,
        activo=True
    )

    cuota1_disciplina2 = board.create_cuota(
        nro_cuota=1,
        estado_pago=0,
        fecha_vencimiento=parse('2022-01-10 22:00:00'),
        valor_cuota=500,
        activo=True
    )

    cuota2_disciplina2 = board.create_cuota(
        nro_cuota=2,
        estado_pago=0,
        fecha_vencimiento=parse('2022-02-10 22:00:00'),
        valor_cuota=520,
        activo=True
    )

    cuota3_disciplina2 = board.create_cuota(
        nro_cuota=3,
        estado_pago=0,
        fecha_vencimiento=parse('2022-03-10 22:00:00'),
        valor_cuota=550,
        activo=True
    )

    cuota1_socio2 = board.create_cuota(
        estado_pago=0,
        fecha_vencimiento=parse('2022-01-10 22:00:00'),
        valor_cuota=500,
        activo=True
    )

    cuota2_socio2 = board.create_cuota(
        estado_pago=0,
        fecha_vencimiento=parse('2022-02-10 22:00:00'),
        valor_cuota=520,
        activo=True
    )

    cuota3_socio2 = board.create_cuota(
        estado_pago=0,
        fecha_vencimiento=parse('2022-03-10 22:00:00'),
        valor_cuota=520,
        activo=True
    )

    pago1 = board.create_pago(
        fecha=parse('2022-10-05 22:00:00'),
        monto=1020,
    )

    board.pago_assign_cuotas(pago1, [cuota1_disciplina2, cuota2_disciplina2])

    board.socio_assign_disciplina(socio1, t_disciplina)
    board.socio_assign_disciplina(socio1, t_disciplina2)
    board.socio_assign_disciplina(socio1, t_disciplina3)
    board.socio_assign_disciplina(socio2, t_disciplina2)
    board.socio_assign_disciplina(socio2, t_disciplina3)

    board.inscripion_assign_cuotas(
        socio1, t_disciplina, [cuota_enero, cuota_febrero, cuota_marzo])

    board.inscripion_assign_cuotas(
        socio1, t_disciplina2, [cuota1_disciplina2, cuota2_disciplina2, cuota3_disciplina2])

    board.inscripion_assign_cuotas(
        socio2, t_disciplina2, [cuota1_socio2, cuota2_socio2, cuota3_socio2])
    board.asignar_rol(1, 1)
    board.asignar_rol(2, 2)
