from flask_restful import Resource, request

class NivelController(Resource):
    # GET, POST, PUT
    def get(self):
        return{
            'message': 'Hola desde el GET de nivel'
        }