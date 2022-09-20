from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import Message, Chat
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers

#@login_required(login_url='/login/')
def index(request):                                                                                 # def heißt define
    if not request.user.is_authenticated:
       return redirect('/logout/')
    if request.method == 'POST':
        print('Received data: ' + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        new_message = Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
        serialized_obj = serializers.serialize('json', [ new_message ])
        return JsonResponse(serialized_obj[1:-1], safe=False)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessages})           # templates/chat/index.html steht da quasi, da die views.py immer in nach templates folder sucht


def loginView(request):
    if request.user.is_authenticated:
        return redirect('/chat/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/chat/')
        else:
            return render(request, 'auth/login.html', {'invalidLogin': True})
    return render(request, 'auth/login.html')


def logoutView(request):
    logout(request)
    return render(request, 'auth/logout.html') 
      

