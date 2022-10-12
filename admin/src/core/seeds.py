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
    
    ##Disciplinas
    t_disciplina = board.create_disciplina(
        id = "1",
        nombre = "Futbol",
        categoria = "2010",
        instructor = "Cosme fulanito",
        dia = "martes",
        hora = "17 Hs",
        costo = "5000"
    ) 

    t_disciplina2 = board.create_disciplina(
        id = "3",
        nombre = "Bascket",
        categoria = "Mini",
        instructor = "Cosme fulanito",
        dia = "Viernes",
        hora = "16 Hs",
        costo = "3000"
    )

    t_disciplina3 = board.create_disciplina(
        id = "7",
        nombre = "Bascket",
        categoria = "Mini",
        instructor = "Cosme fulanito",
        dia = "Viernes",
        hora = "17 Hs",
        costo = "4000",
    ) 