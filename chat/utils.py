from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
def get_userdata_as_json(request, new_message):
    user =  {'user':request.user.username}
    serialized_obj = serializers.serialize('json',  [new_message] )
    json_string = json.dumps({'data': [serialized_obj[1:-1], user]})
    return HttpResponse(json_string, content_type='application/json')


def create_user_and_assing_data(firstname,lastname,username,email,password):
    user = User.objects.create_user(firstname, email, password)
    user.first_name = firstname
    user.last_name = lastname
    user.username = username
    user.save()
    return user

def set_variables_for_signup(request):
    data = []
    data.append(request.POST['firstname'])
    data.append(request.POST['lastname'])
    data.append(request.POST['email'])
    data.append(request.POST['password1'])
    return data
    
