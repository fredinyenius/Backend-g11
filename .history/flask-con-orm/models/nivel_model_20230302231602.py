from base_de_datos import conexion
from sqlalchemy import Column, types


class Nivel(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    numero = Column(type_=types.Integer, nullable=True, unique=True)
    descripcion = Column(type_=types.Text)

    __tablename__ = 'niveles'
