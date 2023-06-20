from api_config import db

class Cliente(db.Model):
    __tablename__ = "cliente"
    dni = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(500))
    email = db.Column(db.String(150), nullable=True)
    telefono = db.Column(db.String(10), nullable=True)
