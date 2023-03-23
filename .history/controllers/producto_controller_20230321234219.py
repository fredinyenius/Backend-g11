from flask_restful import Resource, request
from flask import send_file
from werkzeug.utils import secure_filename
from os import path
from uuid import uuid4
from db import conexion
from models.producto_model import Producto
from dtos.producto_dto import ProductoDto, MostrarProductoDto

class ImagenController(Resource):
    def post(self):
        print(request.form)
        print(request.files)
        imagen = request.files.get('imagen')
        print(imagen.filename)


        nombre_seguro = secure_filename(uuid4().hex + '-' + imagen.filename)

        imagen.save(path.join('imagen', nombre_seguro))

        return {
            'message' : ' Producto creado exitosamente'
        }
    def get(self, nombre):
        try:
            return send_file(path.join('imagen',nombre))
        except FileNotFoundError:
            return send_file(path.join('imagen','not_found.png'))
   
class ProductosController(Resource):
    def post(self):
        #TODO: Validar q tengamos esa llave en el formuklario llamada 'imagen'
        mimetype_validos = 'image/'
        data = request.form.to_dict()
        #TODO: Validar q solo sean imagenes
        #TODO: Agregar un uuid al nombre de la imagen y sea u nombre valido
        #TODO: No  recibir imagenes q pesen mas de 10 mb
        data['imagen'] = imagen.filename
        try:
            imagen = request.files.get('imagen')

            if mimetype_validos not in imagen.mimetype:
                raise Exception('El archivo no es unn archivo valido')
            
            dto = ProductoDto()

            nombre = secure_filename(uuid4().hex +'_'+ imagen.filename) 
 
            data['imagen'] = 'imagen/' + nombre
            data_serializada = dto.load(data)


            nuevo_producto = Producto(**data_serializada)
            conexion.session.add(nuevo_producto)


            imagen.save(path.join('imagen', data['imagen']))
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
        resultado = conexion.session.query(Producto).all()
        dto = MostrarProductoDto()
        data = dto.dump(resultado, many=True)
        return {
            'content': data
        }