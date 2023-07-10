#from django.shortcuts import render
#from django.shortcuts import redirect, render
#from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#from django import forms
from django.http import HttpResponse, JsonResponse
#from django.contrib.auth import login as auth_login
#from .models import Project, Task

from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login

# Importar las clases de forms.py para el formulario de registro.
from blog.forms.custom_forms import CustomUserCreationForm


from .models import Project, Task




# Create your views here.

def index (request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def hello(request, username):
    print(username)
    return HttpResponse("Hello %s" % username)

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html')

def tasks(request):
    # tasks = Task.objects.get(title)
    return render(request, 'tasks.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})






# Función para registrarse como usuario
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.register_user(request)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


