from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#db = SQLAlchemy()

app = Flask(__name__)
conexion = SQLAlchemy(app=app)

if __name__ == '__main__':
    app.run(debug=True)