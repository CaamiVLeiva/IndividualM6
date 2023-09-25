from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request, 'onlinecourse/index.html')

def user_list(request):
    users= User.objects.all() #Para obtener todos los usuarios.
    return render (request, 'onlinecourse/user_list.html', {'users': users})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    
    return render(request, 'onlinecourse/register.html', {'form': form})
