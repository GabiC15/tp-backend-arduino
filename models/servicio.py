from api_config import db

class Servicio(db.Model):
    __tablename__ = "servicio"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    descripcion = db.Column(db.String(250))
    telefono = db.Column(db.String(10), nullable=True)
    web = db.Column(db.String(150), nullable=True)
