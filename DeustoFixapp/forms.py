from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from DeustoFixapp.models import Empleado, Incidencia, Instalacion


class InstalacionForm(ModelForm):
    class Meta:
        model = Instalacion
        fields = '__all__'


class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'


class IncidenciaForm(ModelForm):
    class Meta:
        model = Incidencia
        fields = '__all__'



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

