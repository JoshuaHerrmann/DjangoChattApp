from django.shortcuts import render

def index(request): 
    return render(request, 'chat/index.html')           # templates/chat/index.html steht da quasi, da die views.py immer in nach templates folder sucht
    


