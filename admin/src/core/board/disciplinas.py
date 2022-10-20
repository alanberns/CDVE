from datetime import datetime
from admin.src.web.controllers.disciplinas import disciplinas_index

from src.core.database import db

Class Disciplina(db.Model):

    __tablename__ = "disciplinas"
    id = db.column(db.Integer, primary_key=True, unique=True)
    nombre = db.column(db.String(50))
    categoria = db.column(db.String(50))
    Instructor = db.column(db.String((50)))
    Dia = db.column(db.Datetime)
    Hora = db.column(db.Time)
    Costo = db.column(db.Tnteger)

