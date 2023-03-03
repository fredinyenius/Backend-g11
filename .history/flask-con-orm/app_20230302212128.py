from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import environ
load_dotenv()# es en el encargado de leer el archivo .env si es que existe y agregar las variables en ese archivo como si fuera variables de entorno

print(environ)
#db = SQLAlchemy()

app = Flask(__name__)
print(app.config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/colegio'
conexion = SQLAlchemy(app=app)

if __name__ == '__main__':
    app.run(debug=True)