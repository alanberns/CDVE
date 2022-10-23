from flask import Blueprint, flash
from flask import render_template
from src.core.board import disciplina
from src.core.board.disciplina import Disciplina
from flask import request
from src.core import board
from src.core.board.database import db


disciplina_blueprint = Blueprint("disciplinas", __name__, url_prefix="/disciplinas")


@disciplina_blueprint.get("/")
def disciplina_index():
    
    disciplinas = board.list_disciplinas()
    return render_template("issues/disciplinas.html",disciplinas= disciplinas)
    

@disciplina_blueprint.post("/")
def newdcp():
    kwargs = {
             "nombre":request.form.get("nombre"),
             "categoria":request.form.get("categoria"),
             "entrenador":request.form.get("entrenador"),
             "dia":request.form.get("dia"),
             "hora":request.form.get("hora"),
             "costo_mensual":request.form.get("costo_mensual"),
             "estado":"Activo",
            } 
    board.create_disciplina(**kwargs)
    disciplinas = board.list_disciplinas()
    return render_template("issues/disciplinas.html", disciplina=disciplinas)
   

#parte nueva 

@disciplina_blueprint.post('/deleteds/<id>')
def deletedis(id):
        disciplina = Disciplina.query.get(id)
        disciplina.estado = "Inactivo"
        db.session.commit()
        flash("Disciplina dada de Baja")
        return render_template("issues/disciplinas.html")
   
   





