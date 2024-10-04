from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import AuthenticationForm

class crear_Usuarios_forms(forms.Form):
    nombre_usuario = forms.CharField(max_length=30)
    email_usuario = forms.EmailField()
    
class crear_Productos_forms(forms.Form):
    nombre_producto = forms.CharField(max_length=30)
    marca_producto = forms.CharField(max_length=20)
    
class crear_Ventas_detalles_forms(forms.Form):
    monto = forms.FloatField()
    fecha_venta = forms.DateField()
    forma_de_pago = forms.CharField(max_length=25)
    producto = forms.ModelChoiceField(queryset=Productos.objects.all())
    usuario = forms.ModelChoiceField(queryset=Usuarios.objects.all())


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repetir Contraseña',widget=forms.PasswordInput)

class Meta:
    model = User
    fields = [
        'username',
        'email',
        'password1',
        'password2'
    ]
help_texts = {k: '' for k in "fields"}

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())