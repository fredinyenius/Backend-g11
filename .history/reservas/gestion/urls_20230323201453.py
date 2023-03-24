from django.urls import path
from .views import PruebaView

# urlpattern > NOMBRE OBLIGATORIO para difinir nuestra rutas
urlpatterns = [
    path('prueba/', PruebaView.as_view()),
    path('otra_prueba/', PruebaView.as_view()),

]