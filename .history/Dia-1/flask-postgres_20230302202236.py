from flask import Flask, request
from psycopg2 import connect

app = Flask(__name__)

conexion = connect(host='localhost', database='pruebas', user= 'postgres', password = 'root')

@app.route('/', methods=['GET'])
def inicial():
    return {
        'message': 'Bienbenido al api'
    }

@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
    if request.method=='GET': 

       
        cursor = conexion.cursor()

        cursor.execute('select * from alumnos;')

        resultado = cursor.fetchall()



        print(resultado)
        alumnos_resultado = []

        for alumnos in resultado:
            info_alumno = {
                'id': alumnos[0],
                'nombre': alumnos[1],
                'apellido': alumnos[2],
                'sexo': alumnos[3],
                'fecha_creacion': alumnos[4],
                'matriculado': alumnos[5],
            }

            alumnos_resultado.append(info_alumno)
    elif request.method == 'POST':
            data = request.json
            print(data)
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO ALUMNOS (nombre, apellido, matriculado) VALUES (%s, %s, %s)",(
                 data.get('nombre'),data.get('apellido'),data.get('matriculado')
           ))
            
            conexion.commit()
            
            return {
        'message': 'Alumnos ingresado exitosamente'
    }
    
@app.route('/alumno/<id>', methods=['GET', 'PUT', 'DELETE'])
def gestion_alumno(id):
     if request.method == 'GET':
          
          cursor = conexion.cursor()
          cursor.execute("SELECT * FROM alumnos WHERE id %s", (id,))
          alumnos = cursor.fetchone()

          if alumnos:
               return{
                    'content': {
                    'id': alumnos[0],
                    'nombre': alumnos[1],
                    'apellido': alumnos[2],
                    'sexo': alumnos[3],
                    'fecha_creacion': alumnos[4],
                    'matriculado': alumnos[5],
                    }
               }
          else:
               return{
                    'message': 'El alumno no existe'
               }

        
if __name__ == '__main__':

    # debug> indicar que cada vez que guardemos un archivo del proyecto el servidor se reinicie automaticamente
    app.run(debug=True)

