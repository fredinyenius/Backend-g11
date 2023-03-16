from flask_restful import Resource, request
from bcrypt import  hashpw, gensalt, checkpw
from sqlalchemy.orm import  Query
from dtos.usuario_dto import UsuarioDto, LoginDto 
from models.usuario_model import Usuario
from bd import conexion

class UsuarioController(Resource):
    def post(self):
        data = request.json
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
        
class LoginController(Resource):
    def post(self):
        data = request.json
        dto = LoginDto()
        try:
            data_validada = dto.load(data)
            # Buscar el usuario por ese correo
            query:Query = conexion.session.query(Usuario)
            usuario_encontrado: Usuario | None =  query.filter_by(correo = data_validada.get('correo')).first()
            if not usuario_encontrado:
                return {
                    'message': 'El usuario no existe'
                }
            # Ahora valido si la contraseña es la correcta
            # Lo convierto a bytes porque asi trabaja la funcion checkpw
            hashed_password = bytes(usuario_encontrado.password,'utf-8')
            password = bytes(data_validada.get('password'), 'utf-8')

            checkpw(password,hashed_password)

        except Exception as error:
            return {
                'message': 'Error al hacer el login',
                'content': error.args
            }