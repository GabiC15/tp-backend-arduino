from api_config import db

class Subscripcion(db.Model):
    __tablename__ = "subscripcion"
    id = db.Column(db.Integer, primary_key=True)
    cuota = db.Column(db.Integer)
    fk_cliente = db.Column(db.Integer, db.ForeignKey("cliente.dni"))
    fk_servicio = db.Column(db.Integer, db.ForeignKey("servicio.id"))
    cliente = db.relationship("Cliente", backref="subcripciones")
    servicio = db.relationship("Servicio", backref="subcripciones")
