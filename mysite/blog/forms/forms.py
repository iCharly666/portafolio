from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from blog.models import CategoriaForo


# Agregar campo email al usuario ya que django no lo tienen en su user por defecto.
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)


# Crear una categoria de foro:


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = CategoriaForo
        fields = ["nombre", "descripcion", "imagen"]


# Custom login form
"""
class CustomLoginForm(AuthenticationForm):
    email = forms.EmailField(label='Correo electrónico')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.HiddenInput()

"""
