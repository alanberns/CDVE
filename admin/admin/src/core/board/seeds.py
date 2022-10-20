from src.core import board

#creamos 3 issues para agregar datos en la tabla

##Disciplinas
def run():
    t_disciplina = board.create_issue(
        id = "1",
        nombre = "Futbol",
        categoria = "2010",
        entrenador = "Carlos Bianchi",
        dia = "Martes",
        hora = "17 Hs",
        costo_mensual = "5000",
        activo = "true",
    )
    t_disciplina2 = board.create_issue(
        id = "2",
        nombre = "Tenis",
        categoria = "Mini",
        entrenador = "Sebastian Coria",
        dia = "Miercoles",
        hora = "16 Hs",
        costo_mensual = "3000",
        activo = "false",
    )
    t_disciplina3 = board.create_issue(
        id = "3",
        nombre = "Basquet",
        categoria = "Sub 19 ",
        entrenador = "Facundo Campazzo",
        dia = "Viernes",
        hora = "17 Hs",
        costo_mensual = "4000",
        activo="True",
    )
    t_disciplina4 = board.create_issue(
        id = "4",
        nombre = "Tenis",
        categoria = "2017 ",
        entrenador = "Rafael Nadal",
        dia = "Jueves",
        hora = "13 Hs",
        costo_mensual = "3400",
        activo="True",
    )
    t_disciplina5 = board.create_issue(
        id = "5",
        nombre = "Handball",
        categoria = "2017 ",
        entrenador = "Gonzalo Carou",
        dia = "Viernes",
        hora = "17 Hs",
        costo_mensual = "3400",
        activo="True",
    )
    t_disciplina5 = board.create_issue(
        id = "6",
        nombre = "Hockey",
        categoria = "Mini",
        entrenador = "Maria Forcherio",
        dia = "Viernes",
        hora = "18 Hs",
        costo_mensual = "4600",
        activo="True",
    )
    t_disciplina5 = board.create_issue(
        id = "7",
        nombre = "Futbol",
        categoria = "2014 ",
        entrenador = "Marcelo Gallardo",
        dia = "Lunes",
        hora = "14 Hs",
        costo_mensual = "7600",
        activo="True",
    )
    