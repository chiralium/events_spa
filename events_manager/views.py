from rest_framework.response import Response
from rest_framework.views import APIView

class Home(APIView):
    def get(self, request): return Response({"error": "Endpoint is not specified!"})


class Register(APIView):
    def get(self, request):
        return Response({
            "message": "Hello World from Django Rest API"
        })
