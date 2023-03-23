from flask_restful import Resource, request
from db import conexion
from models.producto_model import Producto

class ProductosController(Resource):
    def post(self):
        pass
