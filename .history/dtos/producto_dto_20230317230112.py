from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.producto_model import Producto

class ProductoDto(SQLAlchemyAutoSchema):
    class Meta:
        # Sirve para crear mi dto que ahora queremos q tambien reconozca las columnas q sean fk
        include_fk = True
        model = Producto