from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from controllers.usuario_controller import UsuarioController, LoginController
from bd import conexion

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/tareas'

app.config['JWT_SECRET_KEY'] = 'ultrasupersecreto'

api = Api(app)

conexion.init_app(app)

Migrate(app=app,db =conexion)
JWTManager(app)
#DEFINIR PROYECTO

api.add_resource(UsuarioController, '/registro')
api.add_resource(LoginController, '/login')

if __name__ == '__main__':
    app.run(debug=True)