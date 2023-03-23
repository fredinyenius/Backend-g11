from flask_restful import Resource, request
from db import conexion
from models.producto_model import Producto
from dtos.producto_dto import ProductoDto

class ProductosController(Resource):
    def post(self):
        data = request.json
        imagen = request.files.get('imagen')
        data['imagen'] = imagen.filename
        try:
            dto = ProductoDto()
            data_serializada = dto.load(data)
            return {
                'message': 'Producto creado exitosamente'
            }
        except Exception as error:
            # si algo fallo todos los inserts, updates y deletes quedaran sin efecto y no se guardara nada en la base de datos
            #conexion.session.rollback()

            return {
                'message': 'Error al registrar el Producto',
                'content': error.args
            }