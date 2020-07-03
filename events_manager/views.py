from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .serializers import EventSerializer
from .models import Event

class Home(APIView):
    def get(self, request): return Response({"error": "Endpoint is not specified!"})

@api_view(['GET', 'POST'])
def registration_handler(request):
    """Registration requests handler"""
    if request.method == 'GET': return Response({"message" : "Undefined request method"});
    elif request.method == 'POST':
        if not __is_fields_valid__([request.data.get('email', None),
                                    request.data.get('password', None)]): return Response({'message' : 'required fields is not specified'})

        if User.objects.filter(email=request.data.get('email')).exists(): return Response({"is_user_exists" : 1})
        else:
            email = request.data.get('email', None)
            password = request.data.get('password', None)

            username = email.split('@')[0]
            User.objects.create_user(email=email, username=username, password=password)
            return Response({"is_user_exists" : 0})

@api_view(['GET', 'POST'])
def login_handler(request):
    """Login requests handler"""
    if request.method == 'GET': return Response({"message" : "Undefined requests method"})
    elif request.method == 'POST':
        if not __is_fields_valid__([request.data.get('email', None),
                                    request.data.get('password', None)]): return Response({'message' : 'required fields is not specified'})

        username = request.data.get('email').split('@')[0]
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'logged_in' : 1})
        else: return Response({'logged_in' : 0})

@api_view(['GET'])
def is_logged_in(request): return Response({"is_authenticated" : request.user.is_authenticated})

@api_view(['GET'])
def get_user_credentials(request):
    if request.user.is_authenticated: return Response({"username" : request.user.username})
    return Response({"username" : False})


@api_view(['GET'])
def logout_handler(request):
    logout(request)
    return Response({"message" : "ok"})

@api_view(['GET'])
def get_all_events(request):
    if request.user.is_authenticated:
        events = Event.objects.filter(event_author=request.user.id)
        serialized_events = EventSerializer(events, many=True)
        return Response({"events" : serialized_events.data})
    return Response({"error" : "User is not authenticated"})

def __is_fields_valid__(fieldset):
    """Check the field by None"""
    for field in fieldset:
        if field is None: return False
    return True
