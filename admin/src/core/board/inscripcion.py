from src.core.database import db


class Inscripcion(db.Model):

    __tablename__ = "inscripciones"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    socio_id = db.Column(db.ForeignKey("socios.id"))

    disciplina_id = db.Column(db.ForeignKey("disciplinas.id"))

    socio = db.relationship(
        "Socio", back_populates="disciplina")
    disciplina = db.relationship(
        "Disciplina", back_populates="socio")
    cuota = db.relationship('Cuota', back_populates="inscripcion")
