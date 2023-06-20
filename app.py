

# from flask import Flask, request

# from conexion import (
#     conect_to_db,
#     db_params,
#     get_all_persons,
#     get_by_id,
#     delete_by_id,
#     update_person_email,
#     get_person_deptos,
#     insert_person,
# )



# app = Flask('Api Test')




# @app.route('/connect')
# def conect():
#     conect_to_db(db_params)
#     return 'Connected to the database'

# @app.route('/all_persons')
# def all_persons():
#     response = get_all_persons()
#     return response


# @app.route('/get_person_by_id')
# def get_person_by_id():
#     id = request.args['id']
#     response = get_by_id(id)
#     return response

# @app.route('/get_person_deptos')
# def get_person_deptos_route():
#     id = request.args['id']
#     response = get_person_deptos(id)
#     return response

# @app.route('/insert_person')
# def insert_person_route():
#     name = request.args['name']
#     last_name = request.args['last_name']
#     if 'email' in request.args:
#         email = request.args['email']
#     else:
#         email = None
#     response = insert_person(name, last_name, email)
#     return f'new person add to database with id {str(response)}'

# @app.route('/delete_person_by_id')
# def delete_person_by_id():
#     id = request.args['id']
#     delete_by_id(id)
#     return "delete successfuly"

# @app.route('/update_mail_person')
# def update_person_mail():
#     id = request.args['id']
#     email = request.args['email']
#     update_person_email(id, email)
#     return f'email address updated'

 
from flask_graphql import GraphQLView

from api_config import (
    app,
    db,
)
from models.schema import schema

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  #? Habilita la interfaz GraphiQL
    )
)

@app.route('/', methods=['GET', 'POST', 'PUT'])
def index():
    return 'Hola Mundo desde Flask Server'

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)