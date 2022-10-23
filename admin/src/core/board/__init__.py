from parser import issuite
from src.core.board.disciplina import Disciplina
#from src.core.board.issue  import Issues
from src.core.board.database import db

def list_disciplinas():
    return Disciplina.query.all()


def create_disciplina(**kwargs):
   disciplina = Disciplina(**kwargs)
   db.session.add(disciplina)
   db.session.commit()

#parte nueva 

def delete_disciplina(id):
   disciplina = Disciplina.query.get(id)
   disciplina.estado = "Inactivo",
   db.session.commit()

  

