from src.core.database import db


class Disciplina(db.Model):

    __tablename__ = "disciplinas"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nombre = db.Column(db.String(50))
    # categoria = db.column(db.String(50))
    # Instructor = db.column(db.String((50)))
    # Dia = db.column(db.Datetime)
    # Hora = db.column(db.Time)
    # Costo = db.column(db.Tnteger)
    socio = db.relationship(
        'Inscripcion', back_populates='disciplina')
