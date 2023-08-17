from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comentario

class ZonaNorteForm(forms.Form):
    nombre = forms.CharField(label="Nombre del lugar", max_length=50, required=True)
    localidad = forms.CharField(label="Localidad", max_length=50, required=True)
    telefono = forms.IntegerField(label="Ingrese nro telefono", required=True)
    deporte = forms.CharField(label="Ingrese el deporte", required=True)
    
class ZonaOesteForm(forms.Form):
    nombre = forms.CharField(label="Nombre del lugar", max_length=50, required=True)
    localidad = forms.CharField(label="Localidad", max_length=50, required=True)
    telefono = forms.IntegerField(label="Ingrese nro telefono", required=True)
    deporte = forms.CharField(label="Ingrese el deporte", required=True)

class ZonaSurForm(forms.Form):
    nombre = forms.CharField(label="Nombre del lugar", max_length=50, required=True)
    localidad = forms.CharField(label="Localidad", max_length=50, required=True)
    telefono = forms.IntegerField(label="Ingrese nro telefono", required=True)
    deporte = forms.CharField(label="Ingrese el deporte", required=True)

class CabaForm(forms.Form):
    nombre = forms.CharField(label="Nombre del lugar", max_length=50, required=True)
    localidad = forms.CharField(label="Localidad", max_length=50, required=True)
    telefono = forms.IntegerField(label="Ingrese nro telefono", required=True)
    deporte = forms.CharField(label="Ingrese el deporte", required=True)
    

class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    nombre = forms.CharField(label="Nombre", required=True)
    apellido = forms.CharField(label="Apellido", required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'nombre', 'apellido', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        
        
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar e-mail")
    first_name = forms.CharField(label="Modificar nombre", required=True)
    last_name = forms.CharField(label="Modificar apellido", required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)
    

#----------------------------------------

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
