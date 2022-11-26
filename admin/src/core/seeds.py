from src.core import board
from dateutil.parser import parse
from datetime import datetime


def run():

    t_disciplinaf1 = board.create_disciplina(
        nombre="Futbol",
        categoria="Mini(2-6)",
        entrenador="Enzo Acosta",
        dia="Martes",
        hora="13 Hs",
        costo_mensual=5000,
        estado=True,
    )

    t_disciplinaf3 = board.create_disciplina(
        nombre="Futbol",
        categoria="Chicos(6-12)",
        entrenador="Nicolas Dematei",
        dia="Martes",
        hora="14 Hs",
        costo_mensual=7000,
        estado=True,
    )

    t_disciplinaf5 = board.create_disciplina(
        nombre="Futbol",
        categoria="Jovenes(13-17)",
        entrenador="Mariano Barbieri",
        dia="Jueves",
        hora="18 Hs",
        costo_mensual=10000,
        estado=False,
    )

    t_disciplinaf7 = board.create_disciplina(
        nombre="Futbol",
        categoria="Adultos(18-40)",
        entrenador="Emiliano Franco",
        dia="Miercoles",
        hora="12 Hs",
        costo_mensual=12000,
        estado=True,
    )

    t_disciplinaf9 = board.create_disciplina(
        nombre="Futbol",
        categoria="Mayores(+ 40)",
        entrenador="Lucas Blondel",
        dia="Jueves",
        hora="13 Hs",
        costo_mensual=13000,
        estado=False,
    )

    t_disciplinat1 = board.create_disciplina(
        nombre="Tenis",
        categoria="Mini(2-6)",
        entrenador="Maria Teran",
        dia="Viernes",
        hora="12 Hs",
        costo_mensual=6000,
        estado=False,
    )

    t_disciplinat3 = board.create_disciplina(
        nombre="Tenis",
        categoria="Chicos(6-12)",
        entrenador="Alberto Mancini",
        dia="Jueves",
        hora="15 Hs",
        costo_mensual=12000,
        estado=True,
    )

    t_disciplinat4 = board.create_disciplina(
        nombre="Tenis",
        categoria="Jovenes(13-17)",
        entrenador="Paola Suarez",
        dia="Miercoles",
        hora="12 Hs",
        costo_mensual=10000,
        estado=True,
    )

    t_disciplinat6 = board.create_disciplina(
        nombre="Tenis",
        categoria="Adultos(18-40)",
        entrenador="Franco Davin",
        dia="Martes",
        hora="11 Hs",
        costo_mensual=12000,
        estado=False,
    )

    t_disciplinat8 = board.create_disciplina(
        nombre="Tenis",
        categoria="Mayores(+ 40)",
        entrenador=" Hernan Gumy",
        dia="Jueves",
        hora="17 Hs",
        costo_mensual=13000,
        estado=True,
    )

    t_disciplinab3 = board.create_disciplina(
        nombre="Boxeo",
        categoria="Jovenes(13-17)",
        entrenador="Omar Narvaez",
        dia="Miercoles",
        hora="17 Hs",
        costo_mensual=10000,
        estado=False,
    )

    t_disciplinab5 = board.create_disciplina(
        nombre="Boxeo",
        categoria="Adultos(18-40)",
        entrenador="Eduardo Lausse",
        dia="Martes",
        hora="10 Hs",
        costo_mensual=12000,
        estado=True,
    )

    t_disciplinab7 = board.create_disciplina(
        nombre="Boxeo",
        categoria="Mayores(+ 40)",
        entrenador="Patricia Quirico",
        dia="Lunes",
        hora="11 Hs",
        costo_mensual=13000,
        estado=True,
    )

    t_disciplinabq1 = board.create_disciplina(
        nombre="Basquet",
        categoria="Mini(2-6)",
        entrenador="Facundo Campazzo",
        dia="Lunes",
        hora="19 Hs",
        costo_mensual=7000,
        estado=True,
    )

    t_disciplinabq3 = board.create_disciplina(
        nombre="Basquet",
        categoria="Chicos(6-12)",
        entrenador="Marcos Delia",
        dia="Lunes",
        hora="11 Hs",
        costo_mensual=6000,
        estado=False,
    )

    t_disciplinabq5 = board.create_disciplina(
        nombre="Basquet",
        categoria="Jovenes(13-17)",
        entrenador="Alberto Finger",
        dia="Sabado",
        hora="16 Hs",
        costo_mensual=10000,
        estado=True,
    )

    t_disciplinabq7 = board.create_disciplina(
        nombre="Basquet",
        categoria="Adultos(18-40)",
        entrenador="Nestor Garcia",
        dia="Martes",
        hora="10 Hs",
        costo_mensual=12000,
        estado=True,
    )

    t_disciplinabq9 = board.create_disciplina(
        nombre="Basquet",
        categoria="Mayores(+ 40)",
        entrenador="Juan Fava",
        dia="Martes",
        hora="19 Hs",
        costo_mensual=13000,
        estado=False,
    )

    t_disciplinav2 = board.create_disciplina(
        nombre="Voley",
        categoria="Mini(2-6)",
        entrenador="Matias Sanchez",
        dia="Lunes",
        hora="10 Hs",
        costo_mensual=6000,
        estado=True,
    )

    t_disciplinav4 = board.create_disciplina(
        nombre="Voley",
        categoria="Chicos(6-12)",
        entrenador=" Ezequiel Palacios",
        dia="Sabados",
        hora="10 Hs",
        costo_mensual=7000,
        estado=False,
    )

    t_disciplinav6 = board.create_disciplina(
        nombre="Voley",
        categoria="Jovenes(13-17)",
        entrenador="Emilia Balague",
        dia="Jueves",
        hora="19 Hs",
        costo_mensual=12000,
        estado=False,
    )

    t_disciplinav7 = board.create_disciplina(
        nombre="Voley",
        categoria="Adultos(18-40)",
        entrenador="Milena Margaria",
        dia="Sabados",
        hora="10 Hs",
        costo_mensual=11000,
        estado=True,
    )

    t_disciplinav8 = board.create_disciplina(
        nombre="Voley",
        categoria="Mayores(+ 40)",
        entrenador="Victoria Caballero",
        dia="Miercoles",
        hora="18 Hs",
        costo_mensual=18000,
        estado=True,
    )

    t_disciplinan1 = board.create_disciplina(
        nombre="Natacion",
        categoria="Mini(2-6)",
        entrenador="Alberto Zorrilla",
        dia="Lunes",
        hora="10 Hs",
        costo_mensual=10000,
        estado=True,
    )

    t_disciplinan3 = board.create_disciplina(
        nombre="Natacion",
        categoria="Chicos(6-12)",
        entrenador="Ana Maria Schultz",
        dia="Miercoles",
        hora="14 Hs",
        costo_mensual=12000,
        estado=True,
    )

    t_disciplinan5 = board.create_disciplina(
        nombre="Natacion",
        categoria="Jovenes(13-17)",
        entrenador="Susana Peper",
        dia="Lunes",
        hora="20 Hs",
        costo_mensual=14000,
        estado=False,
    )

    t_disciplinan7 = board.create_disciplina(
        nombre="Natacion",
        categoria="Adultos(18-40)",
        entrenador="Georgina Bardach",
        dia="Martes",
        hora="11 Hs",
        costo_mensual=16000,
        estado=True,
    )

    t_disciplinap1 = board.create_disciplina(
        nombre="Padel",
        categoria="Chicos(6-12)",
        entrenador="Seba Nerone",
        dia="Martes",
        hora="12 Hs",
        costo_mensual=8000,
        estado=True,
    )

    t_disciplinap3 = board.create_disciplina(
        nombre="Padel",
        categoria="Jovenes(13-17)",
        entrenador="Maria Riera",
        dia="Lunes",
        hora="10 Hs",
        costo_mensual=10000,
        estado=True,
    )

    t_disciplinap5 = board.create_disciplina(
        nombre="Padel",
        categoria="Adultos(18-40)",
        entrenador="Maxi Grabiel",
        dia="Martes",
        hora="18 Hs",
        costo_mensual=12000,
        estado=False,
    )

    t_disciplinap7 = board.create_disciplina(
        nombre="Padel",
        categoria="Mayores(+ 40)",
        entrenador="Martin Di Nenno",
        dia="Lunes",
        hora="15 Hs",
        costo_mensual=14000,
        estado=True,
    )

    t_disciplinay1 = board.create_disciplina(
        nombre="Yoga",
        categoria="Jovenes(13-17)",
        entrenador="Abigail Patron",
        dia="Lunes",
        hora="9 Hs",
        costo_mensual=5000,
        estado=True,
    )

    t_disciplinay3 = board.create_disciplina(
        nombre="Yoga",
        categoria="Adultos(18-40)",
        entrenador="Rita Gutierrez",
        dia="Miercoles",
        hora="12 Hs",
        costo_mensual=7000,
        estado=True,
    )

    t_disciplinay5 = board.create_disciplina(
        nombre="Yoga",
        categoria="Mayores(+ 40 Años)",
        entrenador="Monica Vuchich",
        dia="Lunes",
        hora="10 Hs",
        costo_mensual=6000,
        estado=False,
    )

    t_disciplinak1 = board.create_disciplina(
        nombre="Karate",
        categoria="Chicos(6-12)",
        entrenador="Jenifer Bolado",
        dia="Martes",
        hora="10 Hs",
        costo_mensual=4000,
        estado=True,
    )

    t_disciplinak3 = board.create_disciplina(
        nombre="Karate",
        categoria="Jovenes(13-17)",
        entrenador="Lucia Mariojoulus",
        dia="Miercoles",
        hora="9 Hs",
        costo_mensual=6000,
        estado=True,
    )

    t_disciplinak5 = board.create_disciplina(
        nombre="Karate",
        categoria="Adultos(18-40)",
        entrenador="Francisco Salsench",
        dia="Lunes",
        hora="16 Hs",
        costo_mensual=8000,
        estado=True,
    )

    t_disciplinatk1 = board.create_disciplina(
        nombre="Taekwondo",
        categoria="Chicos(6-12)",
        entrenador="Ezequiel Escobar",
        dia="Lunes",
        hora="13 Hs",
        costo_mensual=6000,
        estado=False,
    )

    t_disciplinatk3 = board.create_disciplina(
        nombre="Taekwondo",
        categoria="Jovenes(13-17)",
        entrenador="Marcos Molina",
        dia="Martes",
        hora="9 Hs",
        costo_mensual=8000,
        estado=True,
    )

    t_disciplinatk5 = board.create_disciplina(
        nombre="Taekwondo",
        categoria="Adultos(18-40)",
        entrenador="Valentina Castro",
        dia="Lunes",
        hora="18 Hs",
        costo_mensual=9000,
        estado=True,
    )


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
    test_user3 = board.create_usuario(
        username="test3",
        email="test3@test3.com",
        password="12345",
        first_name="socio2",
        last_name="Apsocio2",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    # Configuracion
    default_config = board.init_configuracion(
        elementos_pagina=20,
        estado_pago=True,
        texto_recibo="Recibimos de USUARIO el importe en pesos de MONTO por el concepto de cuota societaria de la disciplina DISCIPLINA. A continuacion se detalla lo pagado.",
        valor_base_cuota=1000,
        porcentaje_cuota=0.15,
        email_club="club@gmail.com",
        numero_club="2214151861"
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
    board.rol_assign_permiso(
        rol_administrador,
        [configuracion_all, pago_index, pago_show, pago_update, pago_delete],
    )

    board.rol_assign_permiso(
        rol_operador, [pago_index, pago_show, pago_update])

    # Permisos modulo usuarios
    user_index = board.create_permiso(nombre="user_index")
    user_create = board.create_permiso(nombre="user_create")
    user_delete = board.create_permiso(nombre="user_delete")
    user_update = board.create_permiso(nombre="user_update")
    user_show = board.create_permiso(nombre="user_show")
    user_rol_update = board.create_permiso(nombre="user_rol_update")
    board.rol_assign_permiso(
        rol_administrador,
        [user_index, user_create, user_show,
            user_delete, user_rol_update, user_update],
    )

    # Permisos socios
    socio_index = board.create_permiso(nombre="socio_index")
    socio_create = board.create_permiso(nombre="socio_create")
    socio_delete = board.create_permiso(nombre="socio_delete")
    socio_update = board.create_permiso(nombre="socio_update")
    socio_show = board.create_permiso(nombre="socio_show")
    board.rol_assign_permiso(
        rol_administrador,
        [
            socio_index,
            socio_create,
            socio_show,
            socio_delete,
            socio_update,
        ],
    )

    board.rol_assign_permiso(
        rol_operador,
        [
            socio_index,
            socio_create,
            socio_show,
            socio_delete,
            socio_update,
        ],
    )

    socio1 = board.create_socio(
        id_usuario=1,
        tipo_documento="DNI",
        numero_documento=44556677,
        genero="Femenino",
        direccion="calle falsa 123",
        telefono=14141414,
    )

    socio2 = board.create_socio(
        id_usuario=2,
        tipo_documento="DNI",
        numero_documento=43123123,
        genero="Masculino",
        direccion="7 y 32",
        telefono=221420,
    )

    # Permisos
    permiso_index = board.create_permiso(nombre="index")
    permiso_show = board.create_permiso(nombre="show")
    board.rol_assign_permiso(rol_administrador, [permiso_index, permiso_show])

    # Disciplinas
    t_disciplina = board.create_disciplina(
        nombre="Futbol",
        categoria="2010",
        entrenador="Carlos Bianchi",
        dia="Martes",
        hora="17 Hs",
        costo_mensual="5000",
        estado=True,
    )
    t_disciplina2 = board.create_disciplina(
        nombre="Tenis",
        categoria="Mini",
        entrenador="Sebastian Coria",
        dia="Miercoles",
        hora="16 Hs",
        costo_mensual="3000",
        estado=True,
    )
    t_disciplina3 = board.create_disciplina(
        nombre="Basquet",
        categoria="Sub 19 ",
        entrenador="Facundo Campazzo",
        dia="Viernes",
        hora="17 Hs",
        costo_mensual="4000",
        estado=True,
    )
    t_disciplina4 = board.create_disciplina(
        nombre="Tenis",
        categoria="2017 ",
        entrenador="Rafael Nadal",
        dia="Jueves",
        hora="13 Hs",
        costo_mensual="3400",
        estado=True,
    )
    t_disciplina5 = board.create_disciplina(
        nombre="Handball",
        categoria="2017 ",
        entrenador="Gonzalo Carou",
        dia="Viernes",
        hora="17 Hs",
        costo_mensual="3400",
        estado=True,
    )
    t_disciplina6 = board.create_disciplina(
        nombre="Hockey",
        categoria="Mini",
        entrenador="Maria Forcherio",
        dia="Viernes",
        hora="18 Hs",
        costo_mensual="4600",
        estado=True,
    )

    cuota_enero = board.create_cuota(
        nro_cuota=1,
        estado_pago=0,
        fecha_vencimiento=parse("2022-01-10 22:00:00"),
        valor_cuota=500,
        activo=True,
    )

    cuota_febrero = board.create_cuota(
        nro_cuota=2,
        estado_pago=0,
        fecha_vencimiento=parse("2022-02-10 22:00:00"),
        valor_cuota=520,
        activo=True,
    )

    cuota_marzo = board.create_cuota(
        nro_cuota=3,
        estado_pago=0,
        fecha_vencimiento=parse("2022-03-10 22:00:00"),
        valor_cuota=550,
        activo=True,
    )

    cuota1_disciplina2 = board.create_cuota(
        nro_cuota=1,
        estado_pago=0,
        fecha_vencimiento=parse("2022-01-10 22:00:00"),
        valor_cuota=500,
        activo=True,
    )

    cuota2_disciplina2 = board.create_cuota(
        nro_cuota=2,
        estado_pago=0,
        fecha_vencimiento=parse("2022-02-10 22:00:00"),
        valor_cuota=520,
        activo=True,
    )

    cuota3_disciplina2 = board.create_cuota(
        nro_cuota=3,
        estado_pago=0,
        fecha_vencimiento=parse("2022-03-10 22:00:00"),
        valor_cuota=550,
        activo=True,
    )

    cuota1_socio2 = board.create_cuota(
        nro_cuota=1,
        estado_pago=0,
        fecha_vencimiento=parse("2022-01-10 22:00:00"),
        valor_cuota=500,
        activo=True,
    )

    cuota2_socio2 = board.create_cuota(
        nro_cuota=2,
        estado_pago=0,
        fecha_vencimiento=parse("2022-02-10 22:00:00"),
        valor_cuota=520,
        activo=True,
    )

    cuota3_socio2 = board.create_cuota(
        nro_cuota=3,
        estado_pago=0,
        fecha_vencimiento=parse("2022-03-10 22:00:00"),
        valor_cuota=520,
        activo=True,
    )

    pago1 = board.create_pago(
        fecha=parse("2022-10-05 22:00:00"),
        monto=1020,
    )

    board.pago_assign_cuotas(pago1, [cuota1_disciplina2, cuota2_disciplina2])
    board.socio_assign_disciplina(socio1, t_disciplina)
    board.socio_assign_disciplina(socio1, t_disciplina2)
    board.socio_assign_disciplina(socio1, t_disciplina3)
    board.socio_assign_disciplina(socio2, t_disciplina2)
    board.socio_assign_disciplina(socio2, t_disciplina3)
    board.inscripion_assign_cuotas(
        socio1, t_disciplina, [cuota_enero, cuota_febrero, cuota_marzo]
    )
    board.inscripion_assign_cuotas(
        socio1,
        t_disciplina2,
        [cuota1_disciplina2, cuota2_disciplina2, cuota3_disciplina2],
    )

    board.asignar_rol(rol_administrador.id, test_user.id)
    board.asignar_rol(rol_usuario.id, test_user2.id)
    board.asignar_rol(rol_operador.id, test_user2.id)
    board.asignar_rol(rol_operador.id, test_user3.id)
