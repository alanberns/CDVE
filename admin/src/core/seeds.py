from src.core import board

##Disciplinas
def run():
    t_disciplina = board.create_disciplina(
        nombre = "Futbol",
        categoria = "2010",
        entrenador = "Carlos Bianchi",
        dia = "Martes",
        hora = "17 Hs",
        costo_mensual = 5000,
        estado = True,
    )
    t_disciplina2 = board.create_disciplina(
        nombre = "Tenis",
        categoria = "Mini",
        entrenador = "Sebastian Coria",
        dia = "Miercoles",
        hora = "16 Hs",
        costo_mensual = 3000,
        estado = True,
    )
    t_disciplina3 = board.create_disciplina(
        nombre = "Basquet",
        categoria = "Sub 19 ",
        entrenador = "Facundo Campazzo",
        dia = "Viernes",
        hora = "17 Hs",
        costo_mensual = 4000,
        estado = False,
    )
    t_disciplina4 = board.create_disciplina(
        nombre = "Tenis",
        categoria = "2017 ",
        entrenador = "Rafael Nadal",
        dia = "Jueves",
        hora = "13 Hs",
        costo_mensual = 3400,
        estado = True,
    )
    t_disciplina5 = board.create_disciplina(
        nombre = "Handball",
        categoria = "2017 ",
        entrenador = "Gonzalo Carou",
        dia = "Viernes",
        hora = "17 Hs",
        costo_mensual = 3400,
        estado = False,
    )
    t_disciplina5 = board.create_disciplina(
        nombre = "Hockey",
        categoria = "Mini",
        entrenador = "Maria Forcherio",
        dia = "Viernes",
        hora = "18 Hs",
        costo_mensual = 4600,
        estado = True,
    )
    t_disciplina5 = board.create_disciplina(
        nombre = "Futbol",
        categoria = "2014 ",
        entrenador = "Marcelo Gallardo",
        dia = "Lunes",
        hora = "14 Hs",
        costo_mensual = 7600,
        estado= False,
    )
    