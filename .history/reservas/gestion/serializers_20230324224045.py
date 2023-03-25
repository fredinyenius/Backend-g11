from rest_framework import serializers
from .models import Categoria, Producto
from math import ceil

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


class ProductoConCategoriaSerializers(serializers.ModelSerializer):
        class Meta:
                model = Producto
                fields = '__all__'
                # depth > sirve para indicar que no solamente nos queremos quedar en este modelo sino que mediante la FK
                # queremos acceder a "n" niveles
                depth = 1


def paginationSerializer(totalItems, page, perPage):
        itemsPerPage = perPage if totalItems >= perPage  else totalItems
        totalPages = ceil(totalItems/ itemsPerPage)if itemsPerPage > 0  else None 
        prevPage = page -1 if page > 1 and page < totalPages else  None   
        nextPage = page + 1 if totalPages > 1 and page < totalPages else None   

        return {
                'itemsPerPage': itemsPerPage,
                'totalPages': totalPages,
                'prevPage': prevPage,
                'nextPage': nextPage
        }  