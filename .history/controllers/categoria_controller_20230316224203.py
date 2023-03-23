from flask_restful import Resource, request
from werkzeug.utils import secure_filename
from os import path
from uuid import uuid4

class CategoriasController(Resource):
    def post(self):
        print(request.form)
        print(request.files)
        imagen = request.files.get('imagen')
        print(imagen.filename)


        nombre_seguro = secure_filename(uuid4().hex + '-' + imagen.filename)
        imagen.save(path.join('imagenes', nombre_seguro))

        return {
            'message' : ' Categoria creada exitosamente'
        }