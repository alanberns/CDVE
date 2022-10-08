from flask import Blueprint
from flask import render_template

disciplina_blueprint = Blueprint("disciplinas", __name__, url_prefix="/disciplinas")

@disciplinas_blueprint.get("/")
def disciplina_index():
  issues =   [ 
  { 
       "#id" : 1,
        "Nombre": "Futbol",
        "Categoria": "2010"
        "Instructor": "Cosme Fulanito"
        "Dia": "Martes"
        "Hora": "19 Hs"
        "costo": "3000"
  } 
  { 
       "#id" : 2,
        "Nombre": "Basket",
        "Categoria": "Mini"
        "Instructor": "Cosme Fulanito"
        "Dia": "Viernes"
        "Hora": "16 Hs"
        "costo": "2000"
  } 
  {  
       "#id" : 3,
        "Nombre": "Basket",
        "Categoria": " Pre Mini"
        "Instructor": "Cosme Fulanito"
        "Dia": "Jueves"
        "Hora": "17 Hs"
        "costo": "1500"
   } 
]
