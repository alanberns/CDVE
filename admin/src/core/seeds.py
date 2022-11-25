from src.core import board

def run():

    t_disciplinaf1 = board.create_disciplina(
        nombre = "Futbol",
        categoria = "Mini(2-6)",
        entrenador = "Enzo Acosta",
        dia = "Martes",
        hora = "13 Hs",
        costo_mensual = 5000,
        estado = True,
    )

    t_disciplinaf3 = board.create_disciplina(
        nombre = "Futbol",
        categoria = "Chicos(6-12)",
        entrenador ="Nicolas Dematei",
        dia = "Martes",
        hora = "14 Hs",
        costo_mensual = 7000,
        estado = True,
    )


    t_disciplinaf5 = board.create_disciplina(
        nombre = "Futbol",
        categoria = "Jovenes(13-17)",
        entrenador = "Mariano Barbieri",
        dia = "Jueves",
        hora = "18 Hs",
        costo_mensual = 10000,
        estado = False,
    )
  
    t_disciplinaf7 = board.create_disciplina(
        nombre = "Futbol",
        categoria = "Adultos(18-40)",
        entrenador =  "Emiliano Franco",
        dia = "Miercoles",
        hora = "12 Hs",
        costo_mensual = 12000,
        estado = True,
    )


    t_disciplinaf9 = board.create_disciplina(
        nombre = "Futbol",
        categoria = "Mayores(+ 40)",
        entrenador =  "Lucas Blondel",
        dia = "Jueves",
        hora = "13 Hs",
        costo_mensual = 13000,
        estado = False,
    )

    t_disciplinat1 = board.create_disciplina(
        nombre = "Tenis",
        categoria = "Mini(2-6)",
        entrenador = "Maria Teran",
        dia = "Viernes",
        hora = "12 Hs",
        costo_mensual = 6000,
        estado = False,
    )

    t_disciplinat3 = board.create_disciplina(
        nombre = "Tenis",
        categoria = "Chicos(6-12)",
        entrenador = "Alberto Mancini",
        dia = "Jueves",
        hora = "15 Hs",
        costo_mensual = 12000,
        estado = True,
    )

    t_disciplinat4 = board.create_disciplina(
        nombre = "Tenis",
        categoria = "Jovenes(13-17)",
        entrenador = "Paola Suarez",
        dia = "Miercoles",
        hora = "12 Hs",
        costo_mensual = 10000,
        estado = True,
    )

    t_disciplinat6 = board.create_disciplina(
        nombre = "Tenis",
        categoria = "Adultos(18-40)",
        entrenador = "Franco Davin",
        dia = "Martes",
        hora = "11 Hs",
        costo_mensual = 12000,
        estado = False,
    )

    t_disciplinat8 = board.create_disciplina(
        nombre = "Tenis",
        categoria =  "Mayores(+ 40)",
        entrenador = " Hernan Gumy",
        dia = "Jueves", 
        hora = "17 Hs",
        costo_mensual = 13000,
        estado = True,
    )


    t_disciplinab3 = board.create_disciplina(
        nombre = "Boxeo",
        categoria = "Jovenes(13-17)",
        entrenador = "Omar Narvaez",
        dia = "Miercoles",
        hora = "17 Hs",
        costo_mensual = 10000,
        estado = False,
    )

    t_disciplinab5 = board.create_disciplina(
        nombre = "Boxeo",
        categoria = "Adultos(18-40)",
        entrenador = "Eduardo Lausse",
        dia = "Martes",
        hora = "10 Hs",
        costo_mensual = 12000,
        estado = True,
    )


    t_disciplinab7 = board.create_disciplina(
        nombre = "Boxeo",
        categoria = "Mayores(+ 40)",
        entrenador = "Patricia Quirico",
        dia = "Lunes",
        hora = "11 Hs",
        costo_mensual = 13000,
        estado = True,
    )

    
    t_disciplinabq1 = board.create_disciplina(
        nombre = "Basquet",
        categoria = "Mini(2-6)",
        entrenador = "Facundo Campazzo",
        dia = "Lunes",
        hora = "19 Hs",
        costo_mensual = 7000,
        estado = True,
    )


    t_disciplinabq3 = board.create_disciplina(
        nombre = "Basquet",
        categoria = "Chicos(6-12)",
        entrenador = "Marcos Delia",
        dia = "Lunes",
        hora = "11 Hs",
        costo_mensual = 6000,
        estado = False,
    )


    t_disciplinabq5 = board.create_disciplina(
        nombre = "Basquet",
        categoria = "Jovenes(13-17)",
        entrenador = "Alberto Finger",
        dia = "Sabado",
        hora = "16 Hs",
        costo_mensual = 10000,
        estado = True,
    )

    t_disciplinabq7 = board.create_disciplina(
        nombre = "Basquet",
        categoria = "Adultos(18-40)",
        entrenador = "Nestor Garcia",
        dia = "Martes",
        hora = "10 Hs",
        costo_mensual = 12000,
        estado = True,
    )

    t_disciplinabq9 = board.create_disciplina(
        nombre = "Basquet",
        categoria = "Mayores(+ 40)",
        entrenador = "Juan Fava",
        dia = "Martes",
        hora = "19 Hs",
        costo_mensual = 13000,
        estado = False,
    )

    t_disciplinav2 = board.create_disciplina(
        nombre = "Voley",
        categoria = "Mini(2-6)",
        entrenador = "Matias Sanchez",
        dia = "Lunes",
        hora = "10 Hs",
        costo_mensual = 6000,
        estado = True,
    )


    t_disciplinav4 = board.create_disciplina(
        nombre = "Voley",
        categoria = "Chicos(6-12)",
        entrenador = " Ezequiel Palacios",
        dia = "Sabados",
        hora = "10 Hs",
        costo_mensual = 7000,
        estado = False,
    )

    t_disciplinav6 = board.create_disciplina(
        nombre = "Voley",
        categoria = "Jovenes(13-17)",
        entrenador = "Emilia Balague",
        dia = "Jueves",
        hora = "19 Hs",
        costo_mensual = 12000,
        estado = False,
    )

    t_disciplinav7 = board.create_disciplina(
        nombre = "Voley",
        categoria = "Adultos(18-40)",
        entrenador = "Milena Margaria",
        dia = "Sabados",
        hora = "10 Hs",
        costo_mensual = 11000,
        estado = True,
    )

    t_disciplinav8 = board.create_disciplina(
        nombre = "Voley",
        categoria = "Mayores(+ 40)",
        entrenador = "Victoria Caballero",
        dia = "Miercoles",
        hora = "18 Hs",
        costo_mensual = 18000,
        estado = True,
    )

    t_disciplinan1 = board.create_disciplina(
        nombre = "Natacion",
        categoria = "Mini(2-6)",
        entrenador = "Alberto Zorrilla",
        dia = "Lunes",
        hora = "10 Hs",
        costo_mensual = 10000,
        estado = True,
    )

    t_disciplinan3 = board.create_disciplina(
        nombre = "Natacion",
        categoria = "Chicos(6-12)",
        entrenador = "Ana Maria Schultz",
        dia = "Miercoles",
        hora = "14 Hs",
        costo_mensual = 12000,
        estado = True,
    )

    t_disciplinan5 = board.create_disciplina(
        nombre = "Natacion",
        categoria = "Jovenes(13-17)",
        entrenador = "Susana Peper",
        dia = "Lunes",
        hora = "20 Hs",
        costo_mensual = 14000,
        estado = False,
    )

    t_disciplinan7 = board.create_disciplina(
        nombre = "Natacion",
        categoria = "Adultos(18-40)",
        entrenador = "Georgina Bardach",
        dia = "Martes",
        hora = "11 Hs",
        costo_mensual = 16000,
        estado = True,
    )

    t_disciplinap1 = board.create_disciplina(
        nombre = "Padel",
        categoria = "Chicos(6-12)",
        entrenador = "Seba Nerone",
        dia =  "Martes",
        hora = "12 Hs",
        costo_mensual = 8000,
        estado = True,
    )

    t_disciplinap3 = board.create_disciplina(
        nombre = "Padel",
        categoria = "Jovenes(13-17)",
        entrenador = "Maria Riera",
        dia =  "Lunes",
        hora = "10 Hs",
        costo_mensual = 10000,
        estado = True,
    )

    t_disciplinap5 = board.create_disciplina(
        nombre = "Padel",
        categoria = "Adultos(18-40)",
        entrenador = "Maxi Grabiel",
        dia =  "Martes",
        hora = "18 Hs",
        costo_mensual = 12000,
        estado = False,
    )

    t_disciplinap7 = board.create_disciplina(
        nombre = "Padel",
        categoria = "Mayores(+ 40)",
        entrenador = "Martin Di Nenno",
        dia =  "Lunes",
        hora = "15 Hs",
        costo_mensual = 14000,
        estado = True,
    )

    t_disciplinay1 = board.create_disciplina(
        nombre = "Yoga",
        categoria = "Jovenes(13-17)",
        entrenador = "Abigail Patron",
        dia =  "Lunes",
        hora = "9 Hs",
        costo_mensual = 5000,
        estado = True,
    )


    t_disciplinay3 = board.create_disciplina(
        nombre = "Yoga",
        categoria = "Adultos(18-40)",
        entrenador = "Rita Gutierrez",
        dia =  "Miercoles",
        hora = "12 Hs",
        costo_mensual = 7000,
        estado = True,
    )

    t_disciplinay5 = board.create_disciplina(
        nombre = "Yoga",
        categoria = "Mayores(+ 40 Años)",
        entrenador = "Monica Vuchich",
        dia =  "Lunes",
        hora = "10 Hs",
        costo_mensual = 6000,
        estado = False,
    )

    t_disciplinak1 = board.create_disciplina(
        nombre = "Karate",
        categoria = "Chicos(6-12)",
        entrenador = "Jenifer Bolado",
        dia =  "Martes",
        hora = "10 Hs",
        costo_mensual = 4000,
        estado = True,
    )

    t_disciplinak3 = board.create_disciplina(
        nombre = "Karate",
        categoria = "Jovenes(13-17)",
        entrenador = "Lucia Mariojoulus",
        dia =  "Miercoles",
        hora = "9 Hs",
        costo_mensual = 6000,
        estado = True,
    )

    t_disciplinak5 = board.create_disciplina(
        nombre = "Karate",
        categoria = "Adultos(18-40)",
        entrenador = "Francisco Salsench",
        dia =  "Lunes",
        hora = "16 Hs",
        costo_mensual = 8000,
        estado = True,
    )

    t_disciplinatk1 = board.create_disciplina(
        nombre = "Taekwondo",
        categoria = "Chicos(6-12)",
        entrenador = "Ezequiel Escobar",
        dia =  "Lunes",
        hora = "13 Hs",
        costo_mensual = 6000,
        estado = False,
    )

    t_disciplinatk3 = board.create_disciplina(
        nombre = "Taekwondo",
        categoria = "Jovenes(13-17)",
        entrenador = "Marcos Molina",
        dia =  "Martes",
        hora = "9 Hs",
        costo_mensual = 8000,
        estado = True,
    )

    t_disciplinatk5 = board.create_disciplina(
        nombre = "Taekwondo",
        categoria = "Adultos(18-40)",
        entrenador = "Valentina Castro",
        dia =  "Lunes",
        hora = "18 Hs",
        costo_mensual = 9000,
        estado = True,
    )






