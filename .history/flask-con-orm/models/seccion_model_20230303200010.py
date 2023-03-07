from base_de_datos import conexion
from sqlalchemy import Column, types
from sqlalchemy.sql.schema import ForeignKey


class Seccion(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    alumnos = Column(type_=types.Integer, default=10)

    # si una columno sera utilizada como llave foranea entonces tenemos que utilizar la clase Foreign
    # en ella usaremos el parametro 'column' en el cual indicaremos la tabla

    nivelId = Column(ForeignKey(column='niveles.id'), 
                     type_=types.Integer, nullable=False, name='nivel_id')
    maestroId = Column(ForeignKey(column='maestros.id'), 
                     type_=types.Integer, nullable=False, name='maestro_id')
    

    # como se llamara la tabla en la base de datos
    __tablename__ = 'secciones'