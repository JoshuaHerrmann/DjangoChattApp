from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import Message, Chat
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .utils import get_userdata_as_json, create_user_and_assing_data, set_variables_for_signup




@login_required(login_url='/login/')
def index(request):
    '''
    The main view to render the chat html. Inside the chat each message from model.chat(id) is shown. 
    By sending a new message, a JS response is send to /chat/ and is rendering the new message in the frontend
    '''                                                                               # def heißt define
    #if not request.user.is_authenticated:
    #   return redirect('/logout/')
    if request.method == 'POST':
        print('Received data: ' + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        new_message = Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
        return get_userdata_as_json(request, new_message)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessages})           # templates/chat/index.html steht da quasi, da die views.py immer in nach templates folder sucht


def login_view(request): 
    if request.user.is_authenticated:
        return redirect('/chat/')
    if request.method == 'GET':
        next =  request.GET.get('next', '')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        redirectLink = request.POST['redirectLink']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(redirectLink or '/chat/' )
           #return redirect('/chat/')
        else:
            return render(request, 'auth/login.html', {'invalidLogin': True})
    return render(request, 'auth/login.html',{'redirectLink':next})


def logout_view(request):
    logout(request)
    return render(request, 'auth/logout.html') 


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/chat/')
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            firstname, lastname, email, password = set_variables_for_signup(request)
            username = firstname + lastname
            user = create_user_and_assing_data(firstname,lastname,username,email,password)
            print('Succesfully created new User!',user)
            userLogin = authenticate(request, username=username, password=password)
            login(request, userLogin)
            return redirect('/chat/')
        else:
            return render(request, 'auth/signup.html', {'password_incorrect': True})
    return render(request, 'auth/signup.html')
      

