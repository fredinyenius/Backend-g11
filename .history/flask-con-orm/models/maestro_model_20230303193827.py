from base_de_datos import conexion
from sqlalchemy import Column, types


class Maestro(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    apellido = Column(type_=types.Text)
    correo = Column(type_=types.Text, inique=True, nullable=False)
    direccion = Column(type_=types.Text)

    # como se llamara la tabla en la base de datos
    __tablename__ = 'maestros'