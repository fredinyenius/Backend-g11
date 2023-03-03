from flask import Flask, request
from psycopg2 import connect

app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicial():
    return {
        'message': 'Bienbenido al api'
    }

@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
    if request.method=='GET': 

        conexion = connect(host='localhost', database='pruebas', user= 'postgres', password = 'root')
       
        cursor = conexion.cursor()

        cursor.execute('select * from alumnos;')

        resultado = cursor.fetchall()
        
        print(resultado)
    return {
        'message': 'el resultado'
    }

if __name__ == '__main__':
    # debug> indicar que cada vez que guardemos un archivo del proyecto el servidor se reinicie automaticamente
    app.run(debug=True)
