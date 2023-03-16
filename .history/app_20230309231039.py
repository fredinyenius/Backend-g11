from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from controllers.usuario_controller import UsuarioController
from bd import conexion

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/tareas'

api = Api(app)

conexion.init_app(app)

Migrate(app=app,bd =conexion)
#DEFINIR PROYECTO

api.add_resource(UsuarioController,'/registro')
if __name__ == '__main__':
    app.run(debug=True)