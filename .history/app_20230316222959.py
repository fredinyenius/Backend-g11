from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
from os import environ
from db import conexion
from flask_restful import Api

from utils.enviar_correo import enviar_correo_adjuntos
from controllers.usuario_controller import RegistroController
from controllers.categoria_controller import CategoriasController

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
conexion.init_app(app)
api = Api(app)

Migrate(app, conexion)

@app.route('/prueba')
def enviar_correo_prueba():
    enviar_correo_adjuntos('ederiveroman@gmail.com', 'Correo con imagenes')

    return {
        'message' 'Correo enviado exitosamente'
                }

api.add_resource(RegistroController,'/registro')
api.add_resource(CategoriasController,'/categoria')
if __name__ == '__main__':
    app.run(debug=True)