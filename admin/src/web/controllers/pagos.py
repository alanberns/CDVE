from flask import Blueprint
from flask import render_template

pagos_blueprint = Blueprint("pagos", __name__, url_prefix="/pagos")

@pagos_blueprint.get("/")
def pagos_index():
  issues =   [ 
  { 
       "#idPago" : 570,
        "Socio":  45,
        "Disciplina":  12
        "Periodo": "Octubre"
  } 
  { 
       "#idPago" : 130,
        "Socio":  15,
        "Disciplina":  3
        "Periodo": "Marzo"
  } 
  { 
       "#idPago" : 270,
        "Socio":  55,
        "Disciplina":  5
        "Periodo": "Enero"
  } 
]
