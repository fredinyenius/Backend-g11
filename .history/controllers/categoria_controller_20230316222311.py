from flask_restful import Resource, request

class CategoriasController(Resource):
    def post(self):
        print(request.form)
        print(request.files)

        return {
            'message' : ' Categoria creada exitosamente'
        }