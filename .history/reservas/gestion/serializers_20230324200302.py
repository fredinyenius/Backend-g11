from rest_framework import serializers
from .models import Categoria,Producto

class PruebaSerializers(serializers.Serializer):
        nombre = serializers.CharField(required=True)


class CategoriaSerializers(serializers.ModelSerializer):
        
        class Meta:
                model = Categoria
                fields = '__all__'


class ProductoSerializers(serializers.ModelSerializer):
        
        class Meta:
                model = Producto
                fields = '__all__'