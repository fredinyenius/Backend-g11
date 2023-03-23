from flask_restful import Resource, request

class CategoriasController(Resource):
    def post(self):
        print(request.get_json)
        print(request.files)

        return {
            'message' : 'creado exitosamente'
        }