from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView
from rest_framework import status
from .models import Categoria, Producto
from .serializers import PruebaSerializers, CategoriaSerializers, ProductoSerializers, paginationSerializer, ProductoConCategoriaSerializers


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
        
        print(request.data)
        data = request.data
        data_serializada = PruebaSerializers(data = data)
        #retornara verdadero o faso si la data es correcta
        resultado = data_serializada.is_valid()

        if resultado is True:
            return Response(data = {
                'message':'Se recibio el prueba',
            })
        else:
            return Response(data= {
                'message':'La data es invalida',
                'content': data_serializada.errors()
            })

class CategoriaView(APIView):
    def post(self, request: Request):
        data = request.data

        data_serializada = CategoriaSerializers(data = data)

        resultado = data_serializada.is_valid()
        if resultado:
            print(data_serializada.validated_data)


            nueva_categoria = Categoria(**data_serializada.validated_data)
            # # save() > guarda la nueva informacion en lña base de datos de manera permanente
            nueva_categoria.save()

            return Response(data= {
                'message':'Categoria creada exitosamente'
            })
    
        else:

            return Response(data={
                'message':'Error al crear la categoria',
                'content':data_serializada.errors
            })

    def get(self, request: Request):
        categorias = Categoria.objects.all()
        # NOTA : cuando se pasa  instancias se utiliza el parametro 'instance' y cuando se pasa informacion para validar
        #  se utiliza el parametro 'data'
        data_serializada = CategoriaSerializers(instance=categorias, many=True)
        print(categorias)

        return Response(data={
            # convierta las instancias de la clase  en diccionario
            'content' : data_serializada.data
        })
    
class UnaCategoriaView(APIView):
    def get(self, request: Request, id):
        print(id)
        categoria_encontrada = Categoria.objects.filter(id=id).first()
        if not categoria_encontrada:
            return Response(data={
                  'message': 'categoria no existe'
            }, status=404)
        resultado = CategoriaSerializers(instance=categoria_encontrada)

        return Response(data={
            'content' : resultado.data
            })

    def put(self, request:Request, id):
        
        categoria_encontrada = Categoria.objects.filter(id=id).first()

        if not categoria_encontrada:
            return Response(data={
                  'message': 'categoria no existe'
            }, status=404)

        data =request.data
        data_serializada = CategoriaSerializers(data=data)

        if data_serializada.is_valid():
            categoria_encontrada.nombre = data_serializada.validated_data.get('nombre')
            categoria_encontrada.habilitado = data_serializada.validated_data.get('habilitado')

            categoria_encontrada.save()

            return Response(data={
                'message': 'Categoria actualizada'
                } )
        else :   
            return Response(data={
                'message': 'Error al actulizar la categoria',
                'content' : data_serializada.errors
                })
        

    def delete(self, request:Request, id):
        
        categoria_encontrada = Categoria.objects.filter(id=id).first()

        if not categoria_encontrada:
            return Response(data={
                  'message': 'categoria no existe'
            }, status=404)
        # DELETE FROM categorias WHERE ID = ......;
        # me retorna el total de registros eliminados en una tupla de la sgte manera
        # (correlativo, {'modedlo' : cantidad_elementos_eliminados})
        resultado = Categoria.objects.filter(id =id).delete()
        print(resultado)

        return Response(data={
            'message': 'Categoria eliminada exitosamente'
            })


class ProductosView(APIView):
    def post(self, request: Request):
        data = request.data
        data_serializada = ProductoSerializers(data=data)
        if data_serializada.is_valid():
            nuevo_producto = data_serializada.save()
            
            resultado = ProductoSerializers(instance=nuevo_producto)

            return Response(data={
                'message' : 'Producto creado exitosamente',
                'content' : resultado.data
            },status=status.HTTP_201_CREATED)
        else:
            return Response(data={              
                'message' : 'Error al crear el producto',
                'content' : data_serializada.errors

            },status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request: Request):
        # Pasos para hacer la paginacion maual
        # Primero obtenemos los query params que me serviran para orientarme en la pagina
        page = int(request.query_params.get('page'))
        # 10 > el valor por defecto si no me envia el parametro perPage
        perPage = int(request.query_params.get('perPage', 10))

        # cuantos te vas a saltar
        skip= (page - 1) * perPage

        # cuantos vas tomar, es el mismo valor que perPage
        take= perPage * page


        total_productos = Producto.objects.count()
        
        productos = Producto.objects.all()[skip:take]

        informacion_paginacion = paginationSerializer(total_productos, page, perPage)
        data_serializada = ProductoSerializers(instance=productos, many=True)

        return Response(data={
            'content': data_serializada.data,
            'pageInfo': informacion_paginacion
        },status=status.HTTP_200_OK)
    
class ProductosGenericView(ListAPIView):
    serializer_class = ProductoSerializers
    queryset = Producto.objects.all()

class UnProductoView(APIView):
    def get(self, request:Request, id):
        producto=Producto.objects.get(id=id).first()
        if not producto :
            return Response(data={
                'message': 'Producto no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

        resultado = ProductoConCategoriaSerializers(instance=producto)
        

        return Response(data= {
            'content': resultado.data
        })