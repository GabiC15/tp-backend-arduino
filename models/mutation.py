from graphene import (
    ObjectType,
    Mutation,
    Int,
    String,
    Field,
)
from api_config import (
    db,
)

from .objects import Cliente, Servicio, Subscripcion
from .cliente import Cliente as ClienteModel
from .servicio import Servicio as ServicioModel
from .subscripcion import Subscripcion as SubscripcionModel


class createCliente(Mutation):
    class Arguments:
        dni = Int(required=True)
        first_name = String(required=True)
        last_name = String(required=True)
        email = String(required=False)
        telefono = String(required=False)
    
    cliente = Field(lambda: Cliente)

    def mutate(self, info, dni, first_name, last_name, email=None, telefono=None):
        cliente = ClienteModel(dni=dni, first_name=first_name, last_name=last_name, email=email, telefono=telefono)

        db.session.add(cliente)
        db.session.commit()

        return createCliente(cliente=cliente)

class updateCliente(Mutation):
    class Arguments:
        dni = Int(required=True)
        email = String()
        name = String()
        last_name = String()

    cliente = Field(lambda: Cliente)

    def mutate(self, info, dni, email=None, first_name=None, last_name=None, telefono=None):
        cliente = ClienteModel.query.get(dni)
        if cliente:
            if email:
                cliente.email = email
            if first_name:
                cliente.first_name = first_name
            if last_name:
                cliente.last_name = last_name
            if telefono:
                cliente.telefono = telefono
            db.session.add(cliente)
            db.session.commit()

        return updateCliente(cliente=cliente)


class deleteCliente(Mutation):
    class Arguments:
        dni = Int(required=True)

    cliente = Field(lambda: Cliente)

    def mutate(self, info, dni):
        cliente = ClienteModel.query.get(dni)
        if cliente:
            db.session.delete(cliente)
            db.session.commit()

        return deleteCliente(cliente=cliente)
    
class createServicio(Mutation):
    class Arguments:
        name = String(required=True)
        descripcion = String(required=False)
        telefono = String(required=False)
        web = String(required=False)
    
    servicio = Field(lambda: Servicio)

    def mutate(self, info, name, descripcion, telefono=None, web=None):
        servicio = ServicioModel(name=name, descripcion=descripcion, telefono=telefono, web=web)

        db.session.add(servicio)
        db.session.commit()

        return createServicio(servicio=servicio)

class updateServicio(Mutation):
    class Arguments:
        id = Int(required=True)
        name = String()
        description = String()
        telefono = String()
        web = String()

    servicio = Field(lambda: Servicio)

    def mutate(self, info, id, name=None, description=None, telefono=None, web=None):
        servicio = ServicioModel.query.get(id)
        if servicio:
            if name:
                servicio.name = name
            if description:
                servicio.description = description
            if telefono:
                servicio.telefono = telefono
            if web:
                servicio.web = web
            db.session.add(servicio)
            db.session.commit()

        return updateServicio(servicio=servicio)
    
class deleteServicio(Mutation):
    class Arguments:
        id = Int(required=True)

    servicio = Field(lambda: Servicio)

    def mutate(self, info, id):
        servicio = ServicioModel.query.get(id)
        if servicio:
            db.session.delete(servicio)
            db.session.commit()

        return deleteServicio(servicio=servicio)
    
class createSubscripcion(Mutation):
    class Arguments:
        id_cliente = Int(required=True)
        id_servicio = Int(required=True)
        cuota = Int(required=False)
    
    subscripcion = Field(lambda: Subscripcion)

    def mutate(self, info, id_cliente, id_servicio, cuota):
        subscripcion = SubscripcionModel(fk_servicio=id_servicio, fk_cliente=id_cliente, cuota=cuota)

        db.session.add(subscripcion)
        db.session.commit()

        return createSubscripcion(subscripcion=subscripcion)

class Mutation(ObjectType):
    create_cliente = createCliente.Field()
    update_cliente = updateCliente.Field()
    delete_cliente = deleteCliente.Field()
    create_servicio = createServicio.Field()
    update_servicio = updateServicio.Field()
    delete_servicio = deleteServicio.Field()
    create_subscripcion = createSubscripcion.Field()