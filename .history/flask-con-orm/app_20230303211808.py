# primero se importan las librerias
from flask import Flask
from dotenv import load_dotenv
from os import environ
from flask_migrate import Migrate
from flask_restful import Api
from base_de_datos import conexion
from models.nivel_model import Nivel
from models.maestro_model import Maestro
from models.seccion_model import Seccion
from controllers.nivel_controller import NivelController


load_dotenv() # es en el encargado de leer el archivo .env si es que existe y agregar las variables en ese archivo como si fueran variables de entorno 

app = Flask(__name__)
# dialecto://usuario:password@host:puerto/base_de_datos
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

flask_api = Api(app=app)
# si quiero crear mi conexion en otro archivo e inicializar la configuracion de mi conexion tengo que utilizar el metodo init_app y es aca donde le pasare el parametro de mi instancia de la clase Flask
conexion.init_app(app)

Migrate(app=app, db=conexion)

# defino las rutas  de mi API
flask_api.add_resource(NivelController, '/nivel')

if __name__ == '__main__':
    app.run(debug=True)