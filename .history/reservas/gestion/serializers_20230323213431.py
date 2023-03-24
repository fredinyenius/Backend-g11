from rest_framework import serializers
from .models import Categoria

class PruebaSerializers(serializers.Serializer):
        nombre = serializers.CharField(required=True)


class CategoriaSerializers(serializers.ModelSerializer):
        
        class Meta:
                model = Categoria
                fields = '__all__'