from flask_restful import Resource, request
from bcrypt import gensalt, hashpw
from dtos.usuario_dto import UsuarioDto
from db import conexion
from models.producto_model import Usuario
from utils.enviar_correo import enviar_correo