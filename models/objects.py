from graphene_sqlalchemy import (
    SQLAlchemyObjectType,
)
from graphene import (
    # Int
    String
)

from models.cliente import Cliente as ClienteModel
from models.servicio import Servicio as ServicioModel
from models.subscripcion import Subscripcion as SubscripcionModel

class Cliente(SQLAlchemyObjectType):
    class Meta:
        model = ClienteModel
    name = String(description='representa el nombre del cliente')

class Servicio(SQLAlchemyObjectType):
    class Meta:
        model = ServicioModel

class Subscripcion(SQLAlchemyObjectType):
    class Meta:
        model = SubscripcionModel
