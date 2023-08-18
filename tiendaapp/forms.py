from django import forms

from .models import Categoria, Clientes, Productos 

class CategoriaForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    articulo = forms.IntegerField(required=True)
    

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    categoria = forms.CharField(max_length=100, required=True)
    precio = forms.DecimalField(max_digits=10, decimal_places=3, required=True)
    
    
class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True)
    correo = forms.EmailField(required=True)
    
 
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
    
