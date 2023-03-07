from base_de_datos import conexion
from sqlalchemy import Column, types


class Seccion(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    alumnos = Column(type_=types.Integer, default=10)

    # como se llamara la tabla en la base de datos
    __tablename__ = 'secciones'