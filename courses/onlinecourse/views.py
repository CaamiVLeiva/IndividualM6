from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'onlinecourse/index.html')

def user_list(request):
    users= User.objects.all() #Para obtener todos los usuarios.
    return render (request, 'onlinecourse/user_list.html', {'users': users})