from rest_framework import serializers

class PruebaSerializers(serializers.Serializer):
        nombre = serializers.CharField(required=True)