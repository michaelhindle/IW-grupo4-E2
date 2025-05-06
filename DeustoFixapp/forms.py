import labels
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

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

