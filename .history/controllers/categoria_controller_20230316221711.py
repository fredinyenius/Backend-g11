from flask_restful import Resource, request

class CategoriasController(Resource):
    def post(self):
        print(request.json)
        print(request.files)

        return {
            'message' : 'creado exitosamente'
        }