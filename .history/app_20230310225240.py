from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from datetime import timedelta
from controllers.usuario_controller import UsuarioController, LoginController, PerfilController
from controllers.tarea_controller import TareasController
from bd import conexion

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/tareas'
# Variable de configuracion para JWT
app.config['JWT_SECRET_KEY'] = 'ultrasupersecreto'
# modificando el tiempo de expiration
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1,minutes=10)

api = Api(app)

conexion.init_app(app)

Migrate(app=app,db =conexion)
JWTManager(app)
#DEFINIR PROYECTO

api.add_resource(UsuarioController, '/registro')
api.add_resource(LoginController, '/login')
api.add_resource(PerfilController, '/perfil')
api.add_resource(TareasController, '/tareas')

if __name__ == '__main__':
    app.run(debug=True)