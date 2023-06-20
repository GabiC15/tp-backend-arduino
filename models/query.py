from graphene import (
    ObjectType,
    String,
    Boolean,
    List,
    Int
)

from .objects import Cliente, Servicio, Subscripcion
from .cliente import Cliente as ClienteModel
from .servicio import Servicio as ServicioModel
from .subscripcion import Subscripcion as SubscripcionModel

class Query(ObjectType):
    clientes = List(lambda: Cliente, last_name=String(), dni=Int(), has_email=Boolean(), order_by_name=Boolean())
    servicios = List(lambda: Servicio, id=Int(), order_by_name=Boolean())
    subscripciones = List(lambda: Subscripcion, id=Int(), order_by_name=Boolean())

    def resolve_clientes(self, info, dni=None, last_name=None, has_email=None, order_by_name=None):
        query = Cliente.get_query(info=info)
        if dni:
            query = query.filter(ClienteModel.dni==dni)
        if last_name:
            query = query.filter(ClienteModel.last_name==last_name)
        if has_email is not None:
            if has_email:
                query = query.filter(ClienteModel.email != None)
            else:
                query = query.filter(ClienteModel.email == None)
        if order_by_name:
            query = query.order_by(ClienteModel.name)
        return query.all()
    
    def resolve_servicios(self, info, id=None, order_by_name=None):
        query = Servicio.get_query(info=info)
        if id:
            query = query.filter(ServicioModel.id==id)
        if order_by_name:
            query = query.order_by(ServicioModel.name)
        return query.all()
    
    def resolve_subscripciones(self, info, id=None, order_by_name=None):
        query = Subscripcion.get_query(info=info)
        if id:
            query = query.filter(SubscripcionModel.id==id)
        if order_by_name:
            query = query.order_by(SubscripcionModel.name)
        return query.all()