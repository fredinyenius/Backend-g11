from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.producto_model import Producto

class ProductoDto(SQLAlchemyAutoSchema):
    class Meta:
        model = Producto