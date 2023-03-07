from flask_restful import Resource, request
from sqlalchemy.orm import Query, Session
from base_de_datos import conexion
from models.nivel_model import Nivel

class NivelController(Resource):
    # GET, POST, PUT
    def get(self):
        query: Session = conexion.session(Nivel)
        resultado =query.all()
        print(resultado)
        return{
            'message': 'Hola desde el GET de nivel'
        }