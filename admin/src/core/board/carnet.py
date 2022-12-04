from src.core.database import db


class Carnet(db.Model):

    __tablename__ = "carnets"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    id_socio = db.Column(db.Integer, db.ForeignKey("socios.id"))
    url_imagen = db.Column(db.String(255))
    url_qr = db.Column(db.String(255))

    def __init__(self, id_socio, url_imagen, url_qr):
        self.id_socio = id_socio
        self.url_imagen = url_imagen
        self.url_qr = url_qr
