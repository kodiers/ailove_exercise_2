from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
import json

from .serializers import UserProfileSerializer, UserSerializer, MessageSerializer, RepliesSerializer
from .models import Message, UserProfile, Replies
from .tasks import send_email_task
from .functions import validate_image


# Create your views here.
@csrf_exempt
@require_POST
def login_view(request):
    """
    Login view. If login successful return user information and session id
    :param request: HttpRequest (POST, contains paramters username and password)
    :return: JsonResponse
    """
    error = None
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            serializer = UserSerializer(user)
            session_key = request.session.session_key
            # Form correct dict to reply
            reply = serializer.data
            reply['sessionid'] = session_key
            return JsonResponse(reply)
        else:
            error = "User isn't active"
    else:
        error = "Incorrect username or password"
    return JsonResponse({"error": error})


@csrf_exempt
@require_POST
def create_message(request):
    """
    Create message view. Creates message and send email asynchronously
    :param request: HttpRequest (POST, if user is authenticated contains only subject and text, image is optional,
    else should contains email, name, phone, subject, surname, text)
    :return: JsonResponse
    """
    message = Message()
    if request.user.is_authenticated():
        message.user = request.user
        message.email = request.user.email
        message.name = request.user.first_name
        message.surname = request.user.last_name
        message.phone = request.user.profile.phone
    else:
        message.email = request.POST.get('email')
        message.name = request.POST.get('name')
        message.surname = request.POST.get('surname')
        message.phone = request.POST.get('phone')
    message.subject = request.POST.get('subject')
    message.text = request.POST['text']
    if 'image' in request.FILES and request.FILES['image'] is not None:
        try:
            validate_image(request.FILES['image'])
            message.image = request.FILES['image']
        except ValidationError as e:
            return JsonResponse({'error': e.error_list[0].message})
    message.save()
    send_email_task(message)
    serializer = MessageSerializer(message)
    return JsonResponse(serializer.data)


@csrf_exempt
@require_POST
@login_required
def reply_message(request, message_pk):
    """
    Create reply view. Creates reply and send email to user asynchronously
    :param request: HttpRequest (POST, if user is authenticated contains only text)
    :return: JsonResponse
    """
    message = Message.objects.get(pk=message_pk)
    reply = Replies()
    reply.user = request.user
    reply.message = message
    reply.text = request.POST['text']
    reply.save()
    serializer = RepliesSerializer(reply)
    send_email_task(message, reply)
    return JsonResponse(serializer.data)
