from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Categoria


class PruebaView(APIView):
    def get(self, request):
        data = [ {
            'nombre':'diversion',
            'id':1
        },
         {
            'nombre':'entrenimiento',
            'id':2
        }
        ]
        return Response(data = data)

    def post(self, request: Request):

        return Response(data= {
            'message':'Se recibio el prueba',
        })

class CategoriaView(APIView):
    def post(self, request: Request):
        data = request.data
        nueva_categoria = Categoria(nombre=data.get('nombre'), habilitado = data.get('habilitado'))
        # save() > guarda la nueva informacion en lña base de datos de manera permanente
        nueva_categoria.save()

        return Response(data={
            'message':'Categoria creada exitosamente',
        })

