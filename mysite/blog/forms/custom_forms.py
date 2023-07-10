from django import forms
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from ..models import Project, Task


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return password2

    def register_user(self, request):
        user = self.save(commit=False)
        user.email = self.cleaned_data['email']
        user.save()
        auth_login(request, user)
        print("Usuario registrado:", user.username)
