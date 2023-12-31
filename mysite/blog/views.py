from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404

# from blog.forms.forms import CustomLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseForbidden

# from django.contrib.auth.forms import AuthenticationForm
from blog.models import Project

# Importar clase de formulario personalizado desde la carpeta forms - forms.py
from blog.forms.forms import CustomUserCreationForm

# Decoradores y permisos
from django.contrib.auth.decorators import login_required, permission_required

# Foros
from .models import CategoriaForo
from blog.models import CategoriaForo
from blog.forms.forms import CategoriaForm

import logging

logger = logging.getLogger(__name__)


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def hello(request, username):
    print(username)
    return HttpResponse("Hello %s" % username)


def projects(request):
    projects = list(Project.objects.values())
    return render(request, "projects.html")


def tasks(request):
    return render(request, "tasks.html")


# Función para registrar un usuario mediante formulario y dirigirlo al login una vez se registraron sus datos correctamente.
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


# login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session[
                "username"
            ] = user.username  # Guarda el nombre de usuario en la sesión
            return redirect(
                "/"
            )  # Redirige a la página principal después del inicio de sesión exitoso
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


# logout
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect("index")  # Redirige a la página principal después de cerrar sesión


# Foros
def foros(request):
    categorias = CategoriaForo.objects.all()
    return render(request, "foros.html", {"categorias": categorias})


# Vista para agregar una nueva categoría
@login_required
def crear_categoria(request):
    if request.user.has_perm("blog.crear_categoriaforo"):
        if request.method == "POST":
            form = CategoriaForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # Redirecciona a la página de listado de categorías o a donde desees.
                return redirect("foros")
        else:
            form = CategoriaForm()

        return render(request, "crear_categoria.html", {"form": form})
    else:
        return HttpResponseForbidden(
            "No tienes permisos para agregar categorías, contacta al administrador: ccalderon.tech@gmail.com"
        )


# Vista para editar una categoría existente
@login_required
def editar_categoria(request, categoria_id):
    if request.user.has_perm("blog.editar_entradablog"):
        print("El usuario tiene permiso")
        categoria = get_object_or_404(CategoriaForo, pk=categoria_id)
        if request.method == "POST":
            form = CategoriaForm(request.POST, instance=categoria)
            if form.is_valid():
                form.save()
                return redirect("foros")
        else:
            form = CategoriaForm(instance=categoria)
        return render(
            request, "editar_categoria.html", {"form": form, "categoria": categoria}
        )
    else:
        print("No hay permiso de administrador o usuario no logeado")
        return HttpResponseForbidden(
            "No tienes permisos para editar categorías, contacta al administrador: ccalderon.tech@gmail.com"
        )


# Vista para eliminar una categoría existente
@login_required
def eliminar_categoria(request, categoria_id):
    if request.user.has_perm("blog.eliminar_entradablog"):
        print("El usuario tiene permiso")
        # Código para eliminar una categoria del blog
        categoria = get_object_or_404(CategoriaForo, pk=categoria_id)
        if request.method == "POST":
            categoria.delete()
            return redirect("foros")
        return render(request, "eliminar_categoria.html", {"categoria": categoria})
    else:
        print("No hay permiso de administrador o usuario no logeado")
        return HttpResponseForbidden(
            "No tienes permisos para agregar categorías, contacta al administrador: ccalderon.tech@gmail.com"
        )
