from django import forms

from .models import Categoria, Clientes, Productos 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CategoriaForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    articulo = forms.IntegerField(required=True)
    

class ProductoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100, required=True)
    categoria = forms.CharField(max_length=100, required=True)
    precio = forms.DecimalField(max_digits=10, decimal_places=3, required=True)
    
    
class ClienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100, required=True)
    apellido = forms.CharField(label="Apellido", max_length=100, required=True)
    correo = forms.EmailField(label="Email", required=True)
    
 
#_______________________________________________________________________________________________________


   
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre','articulo']
        
    

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields =['nombre','categoria','precio']
    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields =['nombre','apellido','correo']
    


class RegistroUsuariosForm(UserCreationForm): 
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)
    
class Meta:
   model = User
   fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
   
   
class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)
    