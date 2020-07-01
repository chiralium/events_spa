from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

class Home(APIView):
    def get(self, request): return Response({"error": "Endpoint is not specified!"})

@api_view(['GET', 'POST'])
def registration_handler(request):
    """Registration requests handler"""
    if request.method == 'GET': return Response({"message" : "Undefined request method"});
    elif request.method == 'POST':
        if User.objects.filter(email=request.data.get('email')).exists():
            return Response({"is_user_exists" : 1})
        else:
            email = request.data.get('email', None)
            password = request.data.get('password', None)

            if not (email and password): return Response({'message' : 'required fields is not specified!'})

            username = email.split('@')[0]
            User.objects.create_user(email=email, username=username, password=password)

            return Response({"is_user_exists" : 0})
