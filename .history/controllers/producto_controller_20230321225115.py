from flask_restful import Resource, request
from db import conexion
from models.producto_model import Producto
from dtos.producto_dto import ProductoDto, MostrarProductoDto
from os import path
from sqlalchemy.orm import Query

class ProductosController(Resource):
    def post(self):
        data = request.form.to_dict()
        #TODO: Validar q tengamos esa llave en el formuklario llamada 'imagen'
        #TODO: Validar q solo sean imagenes
        imagen = request.files.get('imagen')
        #TODO: Agregar un uuid al nombre de la imagen y sea u nombre valido
        #TODO: No  recibir imagenes q pesen mas de 10 mb
        data['imagen'] = imagen.filename
        try:
            dto = ProductoDto()
            data_serializada = dto.load(data)
            nuevo_producto = Producto(**data_serializada)
            conexion.session.add(nuevo_producto)
            imagen.save(path.join('imagenes', data['imagen']))

            conexion.session.commit()
            return {
                'message': 'Producto creado exitosamente'
            }
        except Exception as error:
            # si algo fallo todos los inserts, updates y deletes quedaran sin efecto y no se guardara nada en la base de datos
            conexion.session.rollback()

            return {
                'message': 'Error al registrar el Producto',
                'content': error.args
            }
    def get(self):
        #resultado = self.session.query(Producto)
        #query: Query = conexion.session.query(Producto)
        resultado = conexion.session.query(Producto).all()
        dto = MostrarProductoDto()
        data = dto.dump(resultado, many=True)

        return{
            'content': data
        }