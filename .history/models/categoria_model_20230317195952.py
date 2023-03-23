from sqlalchemy import Column , types

from db import conexion

class Usuario(conexion.Model):
    id = Column(type_ =types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    estado = Column(type_=types.Boolean, default=True)
    imagen = Column(type_=types.Text)
   
    __tablename__ = 'usuarios'