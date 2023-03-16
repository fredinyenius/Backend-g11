from flask_restful import Resource, request
from bcrypt import Resource, hashpw, gensalt
from dtos.usuario_dto import UsuarioDto
from models.usuario_model import Usuario
from bd import conexion

class UsuarioController(Resource):
    def post(self):
        data = self.json
        dto = UsuarioDto()
        try:
            data_validata = dto.load(data)
            # Generar el hash de la passworld
            salt = gensalt(rounds=10)
            password = bytes(data_validata.get('password'), 'utf-8')
            password_hashed = hashpw(password, salt)
            password_hashed_str = password_hashed.decode('utf-8')

            nuevo_usuario = Usuario(
                correo = data_validata.get('correo'),
                password = password_hashed_str,
                nombre = data_validata.get('nombre'),
                apellido = data_validata.get('apellido')
            )

            conexion.session.add(nuevo_usuario)
            conexion.session.commit()
            
            Usuario(correo = data_validata.get('correo'),)
            return {
                'message': 'Usuario creado correctamente'
            }
        except Exception as error:
            return{
                'message': 'Error al ingresar el Usuario' ,
                'content': error.args
            }
