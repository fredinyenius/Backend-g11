from flask import Flask
from base_de_datos import conexion
from dotenv import load_dotenv
from os import environ
load_dotenv()# es en el encargado de leer el archivo .env si es que existe y agregar las variables en ese archivo como si fuera variables de entorno



app = Flask(__name__)

print(app.config)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
#si quiero crear mi conexion en otro archivo e inicializacion la 
# confguracion de mi cinexion tengo q utilizaras el metdo init_app
#  y es aca donde le pasare el paramewtro de mi intancia de la clase
#  flask
conexion.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)