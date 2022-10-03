from src.core import board

def run():
    """
    Crea datos por defecto para la base de datos
    """

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
    