#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

from django.shortcuts import render

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





    
    return render(request, 'login.html')
    

def register(request):
    return render(request, 'register.html')
