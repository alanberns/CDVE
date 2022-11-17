from flask import Blueprint
from flask import render_template
from pathlib import Path
from flask import redirect
from flask import url_for
from flask import flash
from flask import request

from src.core.forms.disciplinas_form import DisciplinaNewForm
from src.core.board import disciplina
from src.core import board
from src.core.board.disciplina import Disciplina
#from src.core.database import db



#from src.web.helpers.auth import login_required


disciplina_blueprint = Blueprint("disciplinas", __name__, url_prefix="/disciplinas")

 
@disciplina_blueprint.get ("/")
#@login_required
def disciplina_index():
   elem_pagina = board.get_elementos_pagina()
   page = int(request.args.get('page', 1))
   disciplinas_pag = board.list_disciplinas(page, elem_pagina)
   return render_template('disciplinas.html', disciplinas_pag= disciplinas_pag)

#Se crea una nueva disciplina
@disciplina_blueprint.post("/")
def newdcp():
   form = DisciplinaNewForm(request.form)
   disciplina = board.create_disciplina(
       nombre= form.nombre.data,
       categoria= form.categoria.data,
       entrenador= form.entrenador.data,
       dia = form.dia.data,
       hora = form.hora.data,
       costo_mensual = form.costo_mensual.data,
       estado = True,
   )
   flash ("Se agrego una nueva Disciplina", "success")
   return redirect(url_for('disciplinas.disciplina_index', id=disciplina.id))
    #disciplinas = board.list_disciplinas()
   

@disciplina_blueprint.get("/modifyState/<int:id>")
def modify_state(id):
   board.update_estado_disciplina(id)
   flash ("Se cambio de Estado la Disciplina", "success")
   return redirect(url_for('disciplinas.disciplina_index', id=id))
   

@classmethod
def get_disciplinas():
    disciplinas = Disciplina.list_disciplinas()
    for row in disciplinas:
      disciplina=Disciplina(row[1], row[2], row[3])
      disciplinas.append(disciplina)
    return disciplinas




