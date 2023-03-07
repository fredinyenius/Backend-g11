from flask_restful import Resource, request
from sqlalchemy.orm import Query
from base_de_datos import conexion
from models.nivel_model import Nivel

class NivelController(Resource):
    # GET, POST, PUT
    def get(self):
        query: Query = conexion.session.query(Nivel)
        # SELECT * FROM niveles
        resultado =query.all()
        print(resultado[0].numero)
        print(resultado[0].descriocion)
        return{
            'message': 'Hola desde el GET de nivel'
        }