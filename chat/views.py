from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import Message, Chat
from django.shortcuts import redirect
def index(request): 
    if request.method == 'POST':
        print('Received data: ' + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessages})           # templates/chat/index.html steht da quasi, da die views.py immer in nach templates folder sucht
    
def loginFnc(request):
    if request.method == 'POST':
        print('Try to login')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('logged in!')
            return redirect('/chat/')
        else:
            print('Invalid Login')    
    return render(request, 'chat/login.html')


def logoutFnc(request):
    logout(request)
    print('Logged out') 
    return render(request, 'chat/logout.html') 
      

