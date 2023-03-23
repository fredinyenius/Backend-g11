from flask_restful import Resource, request
from werkzeug.utils import secure_filename

class CategoriasController(Resource):
    def post(self):
        print(request.form)
        print(request.files)
        imagen = request.files.get('imagen')
        print(imagen.filename)
        imagen.save(secure_filename(imagen.filename))

        return {
            'message' : ' Categoria creada exitosamente'
        }