from src.core import board

def run():
    default_config = board.create_or_update_configuracion(
        elementos_pagina = 20,
        estado_pago = True,
        estado_info_contactos = True,
        texto_recibo = "La cuota XXX ha sido pagada",
        valor_base_cuota = 1000,
        porcentaje_cuota = 0.15
    )