from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail

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

            send_mail('Регистрация',
                      'Регистрация прошла успешно, {username}!'.format(username=username),
                      'be2e@yandex.ru',
                      [email], fail_silently=True)

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

@api_view(['POST'])
def create_new_event(request):
    if request.user.is_authenticated:
        request.data.update({'event_author' : request.user.id})
        new_event_data_serializer = EventSerializer(data=request.data)
        if new_event_data_serializer.is_valid():
            new_event_data_serializer.save()
            return Response({"status" : "ok"})
        return Response({"error" : "Data is not valid!"})
    return Response({"error" : "User is not authenticated"})

@api_view(['DELETE'])
def delete_event(request):
    if request.user.is_authenticated:
        event_id = request.data.get('id', None)
        if event_id is None: return Response({"error" : "Required parameter `id` is not passed!"})

        deleted_event = Event.objects.get(pk=event_id, event_author_id=request.user.id)

        if deleted_event is not None: deleted_event.delete()
        else: return Response({"error" : "Event is not found!"})

        return Response({"status" : "Deleted!"})
    return Response({"error" : "User is not authenticated"})

@api_view(['PUT'])
def update_event(request):
    if request.user.is_authenticated:
        event_author = request.user.id
        request.data.update({"event_author": event_author})

        event_id = request.data.get('id', None)
        if event_id is None: return Response({"error" : "Required parameter `id` is not passed!"})

        updated_event = Event.objects.get(pk=event_id)
        updated_event_serializer = EventSerializer(updated_event, data=request.data)

        if updated_event_serializer.is_valid(): updated_event_serializer.save()
        return Response({"status" : "ok"})
    return Response({"error" : "User is not authenticated"})

def __is_fields_valid__(fieldset):
    """Check the field by None"""
    for field in fieldset:
        if field is None: return False
    return True
