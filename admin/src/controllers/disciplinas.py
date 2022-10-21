from flask import Blueprint
from flask import render_template
from src.core.board import disciplina
from flask import request
from src.core import board



disciplina_blueprint = Blueprint("disciplinas", __name__, url_prefix="/disciplinas")

@disciplina_blueprint.get("/")
def disciplina_index():
    
    disciplinas = board.list_disciplinas()
    return render_template("issues/disciplinas.html",disciplinas= disciplinas)
    

@disciplina_blueprint.post("/agregar")
def agregar_disciplina():
    kwargs = {
             "id": request.form.get(id),
             "nombre":request.form.get("nombre"),
             "categoria":request.form.get("categoria"),
             "entrenador":request.form.get("entrenador"),
             "dia":request.form.get("dia"),
             "hora":request.form.get("hora"),
             "costo_mensual":request.form.get("costo_mensual"),
             "estado": request.form.get("estado"),
            } 
    board.create_disciplina(**kwargs)
    disciplinas = board.list_disciplinas()
    return render_template("disciplinas.html", disciplina=disciplinas)
   


@disciplina_blueprint.post("/")
def guardar_disciplina():
    kwargs = {
             "id": request.form.get(id),
             "nombre":request.form.get("nombre"),
             "categoria":request.form.get("categoria"),
             "entrenador":request.form.get("entrenador"),
             "dia":request.form.get("dia"),
             "hora":request.form.get("hora"),
             "costo_mensual":request.form.get("costo_mensual"),
             "estado": request.form.get("estado"),
            } 
    board.create_disciplina(**kwargs)
    disciplinas = board.list_disciplinas()
    return render_template("disciplinas.html", disciplina=disciplinas)
  
 




