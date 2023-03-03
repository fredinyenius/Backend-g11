from flask import Flask
from base-de-datos import conexion
from dotenv import load_dotenv
from os import environ
load_dotenv()# es en el encargado de leer el archivo .env si es que existe y agregar las variables en ese archivo como si fuera variables de entorno



app = Flask(__name__)
print(app.config)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
conexion.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)