from src.core import board

def run():
    """
    Crea datos por defecto para la base de datos
    """

    test_user = board.create_usuario(
        username = "test",
        mail = "test@test.com",
        contraseña = "1234"
    )
    test_user2 = board.create_usuario(
        username = "test2",
        mail = "test2@test2.com",
        contraseña = "1234"
    )
    ###Configuracion
    default_config = board.init_configuracion(
        elementos_pagina = 20,
        estado_pago = True,
        estado_info_contactos = True,
        texto_recibo = "La cuota XXX ha sido pagada",
        valor_base_cuota = 1000,
        porcentaje_cuota = 0.15
    )

    ###Roles
    rol_administrador = board.create_rol(
        nombre = "administrador" 
    )

    ###Permisos
    permiso_index = board.create_permiso(
        nombre = "index" 
    )
    permiso_show = board.create_permiso(
        nombre = "show" 
    )
    board.rol_assign_permiso(rol_administrador,[permiso_index,permiso_show])

    socio1 = board.create_socio(
        id_usuario = 1,
        #el id de usuario debería obtenerse desde el usuario
        tipo_documento = "DNI",
        numero_documento = 44556677,
        genero = "femenino",
        numero_socio = "AAA111",
        direccion = "calle falsa 123",
        telefono = 14141414,
        email = "socio1@mail.com"
        #el usuario tiene mail también, arreglar.
    )
    