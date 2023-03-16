from flask_restful import Resource, request
#from bcrypt import  hashpw, gensalt, checkpw
#from sqlalchemy.orm import  Query
from flask_jwt_extended import jwt_required, get_jwt_identity
#from dtos.tarea_dto import TareaDto 
from models.tarea_model import Tarea
from bd import conexion

class TareasController(Resource ):
    def post(self):
        pass
    def get(self):
        pass