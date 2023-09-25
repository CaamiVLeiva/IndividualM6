from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

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
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'onlinecourse/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    
    return render(request, 'onlinecourse/login.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'onlinecourse/dashboard.html', {'user': request.user})
    else:
        return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('index')
