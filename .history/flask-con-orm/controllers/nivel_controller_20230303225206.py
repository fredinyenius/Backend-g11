from flask_restful import Resource, request
from sqlalchemy.orm import Query
from base_de_datos import conexion
from models.nivel_model import Nivel
from dtos.nivel_dto import NivelDto

class NivelController(Resource):
    # GET, POST, PUT
    def get(self):
        query: Query = conexion.session.query(Nivel)
        # SELECT * FROM niveles
        resultado =query.all()

        dto = NivelDto()
        dto.dump = (resultado, many=True)

        niveles =[]

        #print(resultado[0].numero)
        #print(resultado[0].descripcion)
        #for nivel in resultado:
        #    niveles.append({
        #        'id': nivel.id,
        #        'numero': nivel.numero,
        #        'descripcion': nivel.descripcion
        #    })
        return{
            'content': niveles
        }
    
    def post(self):
        data = request.json
        dto = NivelDto()

        try:
            data_validada = dto.load(data)
            print(data_validada)

            nuevo_nivel = Nivel(numero=data_validada.get('numero'), descripcion=data_validada.get('descripcion'))
            # con el metodo add indicamos que queremos guardar ese nuevo registro
            conexion.session.add(nuevo_nivel)
            # con el metodo commit queremos guardar de manera permanente de la base de datos
            conexion.session.commit()

            return {
            'message': 'Nivel creado exitosamente'
        }, 201
        except Exception as error:
            return{
            'message': 'Error al crear el nivel',
            'content': error.args
            }