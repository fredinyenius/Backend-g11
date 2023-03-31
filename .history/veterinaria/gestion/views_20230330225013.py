from rest_framework.views import APIView
from rest_framework.request import Request
from .serializers import RegistroUsuarioSerializer
from .models import Usuario
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import SoloClientes

class RegistroUsuario(APIView):

    def post(self, request: Request):
        print(request.data)
    
        serializador = RegistroUsuarioSerializer(data = request.data)
        print(serializador.is_valid())
        if serializador.is_valid():
            print(serializador.validated_data)
            password = serializador.validated_data.get('password')
            nuevo_usuario = Usuario(**serializador.validated_data)
            # generar el hash de la password
            print(nuevo_usuario)
            nuevo_usuario.set_password(password)
            nuevo_usuario.save()

            return Response(data={
                'message': 'Usuario creadp exitosamente'
            },status=status.HTTP_201_CREATED)
        else:
            return Response(data= {
                'message': 'Error al crear el usuario',
                'content': serializador.errors
            },status=status.HTTP_400_BAD_REQUEST)
        
class PerfilUsuario(APIView):

    permission_classes = [IsAuthenticated, SoloClientes]

    def get(self, request: Request):
        print(request.user)
        print(request.auth)
        #TODO: Devolver el usuario, NO DEVOLVER LA PASSWORD SOLAMENTE EL  NOMBRE, APELLIDO.
        #  CORREO Y TIPOuSUARIO UTILIZANDO UN SERIALISADOR
        return Response(data={
            'content': ''
        })
    
class Mascotas(APIView):
    permission_classes = [IsAuthenticated, SoloClientes]

    def post(self, request: Request):
        archivos = request.FILES
        print(archivos)

        return Response(data={
            'message': 'Mascota creada exitosamnete'
        },status=status.HTTP_201_CREATED)


# Create your views here.
