from rest_framework.views import APIView
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
        return {
            'content' : data
        }


# Create your views here.
