from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
#from blog.forms.forms import CustomLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
#from django.contrib.auth.forms import AuthenticationForm
from blog.models import Project
# Importar clase de formulario personalizado desde la carpeta forms - forms.py
from blog.forms.forms import CustomUserCreationForm

import logging
logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def hello(request, username):
    print(username)
    return HttpResponse("Hello %s" % username)

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html')

def tasks(request):
    return render(request, 'tasks.html')



# Función para registrar un usuario mediante formulario y dirigirlo al login una vez se registraron sus datos correctamente.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Redirige a la página principal después del inicio de sesión exitoso
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})






