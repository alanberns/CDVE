from flask import Blueprint
from flask import render_template
from src.core.board import disciplina
from flask import request
from src.core import board
from src.core.board.disciplina import Disciplina
from src.core.board.database import db
#from src.web.helpers.auth import login_required


disciplina_blueprint = Blueprint("disciplinas", __name__, url_prefix="/disciplinas")

@disciplina_blueprint.get("/")
#@login_required
def disciplina_index():
   disciplinas = board.list_disciplinas()
   return render_template('disciplinas.html',disciplinas= disciplinas)
 


@disciplina_blueprint.post("/")
def newdcp():
    kwargs = {
             "nombre":request.form.get("nombre"),
             "categoria":request.form.get("categoria"),
             "entrenador":request.form.get("entrenador"),
             "dia":request.form.get("dia"),
             "hora":request.form.get("hora"),
             "costo_mensual":request.form.get("costo_mensual"),
             "estado":"Activa"
            } 
    board.create_disciplina(**kwargs)
    disciplinas = board.list_disciplinas()
    return render_template('disciplinas.html', disciplina=disciplinas)
   

