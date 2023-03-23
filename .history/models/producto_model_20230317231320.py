from sqlalchemy import Column , types
from sqlalchemy.sql.schema import ForeignKey
from db import conexion
from datetime import datetime

class Producto(conexion.Model):
    id = Column(type_ =types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    precio = Column(type_=types.Float)
    imagen = Column(type_=types.Text)
    categoriaId = Column(ForeignKey(column='categorias.id'), type_=types.Integer,
                          nullable=False, name='categoria_id')

    fecha_creacion =Column(type_= types.DateTime, default=datetime.utcnow, name='createdAt')

   
    __tablename__ = 'productos'