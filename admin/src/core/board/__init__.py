from parser import issuite
from src.core.board.disciplina import Disciplina
from src.core.database import db
from sqlalchemy import and_, or_, not_


#Lista todas las disciplinas
def list_disciplinas(page=1, per_page=10):
    return Disciplina.query.order_by(Disciplina.id.asc()).paginate(page=page,per_page=per_page,error_out=False)

def listAll_disciplinas():
  return Disciplina.query.all()

  
# Crea una nueva disciplina
def create_disciplina(**kwargs):
   disciplina = Disciplina(**kwargs)
   db.session.add(disciplina)
   db.session.commit()
   return disciplina

@classmethod
def get_disciplinas(self):
    disciplinas = Disciplina.query.all()
    for row in disciplinas:
      disciplina=Disciplina(row[1], row[2], row[3])
      disciplinas.append(disciplina)
    return disciplinas


# Busca una disciplina por su ID y la devuelve
def get_disciplina(id):
   disciplina = Disciplina.query.filter(Disciplina.id == id).first()
   return disciplina


# Verifica si una disciplina a crear, ya existe.
def find_same_discipline(nombre, categoria, entrenador, dia, hora):
   checkDiscipline = Disciplina.query.filter_by(nombre=nombre, categoria=categoria, entrenador = entrenador, dia=dia, hora=hora,).first()
   return (checkDiscipline)


#Cambia es estado de una disciplina
def update_estado_disciplina(id):
  disciplina = get_disciplina(id)
  disciplina.estado = not (disciplina.estado)
  db.session.commit()
  return disciplina

#Cantidad de elementos de pagina, establecidos en configuracion
def get_elementos_pagina():
  configuracion = Configuracion.query.first()
  return configuracion.elementos_pagina

  
# Actualiza la informacion de una Disciplina  
def updatedisciplina(id, kwargs):
  disciplina = get_disciplina(id)
  disciplina.update(**kwargs)
  db.session.merge(disciplina)
  db.session.commit()
  return disciplina



