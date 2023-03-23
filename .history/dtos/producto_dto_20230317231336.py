from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models.producto_model import Producto
from dtos.categoria_dto import CategoriaDto

class ProductoDto(SQLAlchemyAutoSchema):
    class Meta:
        # Sirve para crear mi dto que ahora queremos q tambien reconozca las columnas q sean fk
        include_fk = True
        model = Producto

class MostrarProductoDto(SQLAlchemyAutoSchema):
    categoriaId = fields.Nested(nested=CategoriaDto)
    class Meta:
        # Sirve para crear mi dto que ahora queremos q tambien reconozca las columnas q sean fk
        include_fk = True
        load_instance = True
        model = Producto