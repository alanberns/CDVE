from parser import issuite
from src.core.board.disciplina import Disciplina
from src.core.database import db


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

#Cambia es estado de una disciplina
def update_estado_disciplina(id):
  disciplina = get_disciplina(id)
  disciplina.estado = not (disciplina.estado)
  db.session.commit()
  return disciplina

#Cantidad de elementos de pagina, establecidos en configuracion
def get_elementos_pagina():
  #configuracion = Configuracion.query.first()
  #return configuracion.elementos_pagina
  elementos_pagina = 10
  return elementos_pagina
  
# Actualiza la informacion de una Disciplina  
def update_disciplina(id, **kwargs):
  disciplina = get_disciplina(id)
  disciplina.update(**kwargs)
  db.session.commit()
  return disciplina


