from flask import Blueprint
from flask import render_template
from src.core.board import issue
from flask import request
from src.core import board


issue_blueprint = Blueprint("issues", __name__, url_prefix="/disciplinas")

@issue_blueprint.get("/")
def issue_index():
    
    issues = board.list_issues()
    return render_template("issues/disciplinas.html", issues=issues)
    

@issue_blueprint.get("agregar_disciplina")
def agregar_disciplina():
    return render_template("issues/nuevaDisciplina.html")

    
@issue_blueprint.post("/")
def guardar_disciplina():
    kwargs = {
             "id": request.form.get("id"),
             "nombre":request.form.get("nombre"),
             "categoria":request.form.get("categoria"),
             "entrenador":request.form.get("entrenador"),
             "dia":request.form.get("dia"),
             "hora":request.form.get("hora"),
             "costo_mensual":request.form.get("costo_mensual"),
            } 
    board.create_issue(**kwargs)
    issues = board.list_issues()
    return render_template("issues/nuevaDisciplina.html")




