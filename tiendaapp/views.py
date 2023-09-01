
from django.http import HttpResponse
from django.shortcuts import  redirect, render, get_list_or_404
from django.urls import reverse_lazy

from .models import Productos , Categoria , Clientes, About, Avatar
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView

from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#from forms import UserEditForm
# Create your views here.


def home(request):
    return render(request, 'tiendaapp/home.html')

@login_required
def categoria(request):
    contexto = {'categoria': Categoria.objects.all(),'titulo': 'Categoria de Productos'}
    return render(request, 'tiendaapp/categoria.html', contexto)

def productos(request):
    contexto = {'productos': Productos.objects.all(),'titulo': 'Lista de Productos en Stock'}
    return render(request, 'tiendaapp/productos.html', contexto)

def clientes(request):
    contexto = {'clientes': Clientes.objects.all(),'titulo': 'Listado de Clientes Registrados'}
    return render(request, 'tiendaapp/clientes.html', contexto)


def about_me(request):
    contexto = {'about_me': About.objects.all()}
    return render(request, 'tiendaapp/about.html', contexto)



 #_________________________________________________________________________________________________________________

@login_required
def categoriaForm(request):
    if request.method == "POST":
        miForm = CategoriaForm(request.POST)
        if miForm.is_valid():
            categoria_nombre = miForm.cleaned_data.get("nombre")
            categoria_articulo = miForm.cleaned_data.get("articulo")           
            categoria = Categoria(nombre=categoria_nombre,
                                 categoria=categoria_articulo)
            categoria.save()
            return render(request, "tiendaapp/base.html")
    else:
        miForm = CategoriaForm()
        
    return render(request, "tiendaapp/categoriaForm.html", {"form": miForm})   

@login_required
def buscarCategoria(request):
    return render(request, "tiendaapp/buscarCategoria.html")

@login_required
def buscarCategoria2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        categoria = Categoria.objects.filter(nombre__icontains=patron)
        contexto = {"categoria": categoria, 'titulo': f'La categoria que tienen como patron "{patron}"'}
        return render(request, "tiendaapp/categoria.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")

#_____________________________________________________________________________________

@login_required   
def productoForm(request):
    if request.method == "POST":
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto_nombre = miForm.cleaned_data.get("nombre")
            producto_categoria = miForm.cleaned_data.get("categoria")
            producto_precio = miForm.cleaned_data.get("precio")
            producto = Productos(nombre=producto_nombre,
                                 categoria=producto_categoria,
                                 precio=producto_precio)
            producto.save()
            return render(request, "tiendaapp/base.html")
    else:
        miForm = ProductoForm()
        
    return render(request, "tiendaapp/productoForm.html", {"form": miForm})


@login_required
def buscarProducto(request):
    return render(request, "tiendaapp/buscarProducto.html")

@login_required
def buscarProducto2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        producto = Productos.objects.filter(nombre__icontains=patron)
        contexto = {"productos": producto, 'titulo': f'Lista de Productos que tienen como patron "{patron}"'}
        return render(request, "tiendaapp/productos.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")

#_____________________________________________________________________________________
@login_required
def clienteForm(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_apellido = miForm.cleaned_data.get("apellido")
            cliente_correo = miForm.cleaned_data.get("correo")
            cliente= Clientes(nombre=cliente_nombre,
                                 apellido=cliente_apellido,
                                 correo=cliente_correo)
            cliente.save()
            return render(request, "tiendaapp/base.html")
    else:
        miForm = ClienteForm()
        
    return render(request, "tiendaapp/clienteForm.html", {"form": miForm})

@login_required
def buscarCliente(request):
    return render(request, "tiendaapp/buscarCliente.html")

@login_required
def buscarCliente2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        cliente = Clientes.objects.filter(nombre__icontains=patron)
        contexto = {"clientes": cliente, 'titulo': f'Lista de Clientes que tienen como patron "{patron}"'}
        return render(request, "tiendaapp/clientes.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")



#______________________________________________________________________________________________________________



@login_required
def agregarProducto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect ( "productos")
        
        
    else:
            producto_form = ProductoForm()
            
    return render(request,'tiendaapp/formularioProducto.html', {'producto_form':producto_form})
            
    
@login_required   
def agregarCliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect ( "clientes")
       
    else:
            cliente_form = ClienteForm()
            
    return render(request,'tiendaapp/formularioCliente.html', {'cliente_form':cliente_form})
            
@login_required    
def agregarCategoria(request):
    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST)
        if categoria_form.is_valid():
            categoria_form.save()
            return redirect ( "categoria")
                 
        
    else:
            categoria_form = CategoriaForm()
            
    return render(request,'tiendaapp/formularioCategoria.html', {'categoria_form':categoria_form})
            


#___________________________________Productos__________Class Based Views


class ProductoList(LoginRequiredMixin, ListView):
    model = Productos
    
class ProductoCreate(LoginRequiredMixin, CreateView):
    model = Productos
    fields = ['nombre', 'categoria', 'precio']
    success_url =  reverse_lazy('productos')
    
class ProductoUpdate(LoginRequiredMixin, UpdateView):
    model = Productos
    fields = ['nombre', 'categoria', 'precio']
    success_url =  reverse_lazy('productos')
    
class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = Productos
    success_url =  reverse_lazy('productos')
    
class ProductoDetail(LoginRequiredMixin, DetailView):
    model = Productos
    template_name = 'tiendaapp/productoDetail.html'
    
    
#___________________________________Clientes______________Class Based Views


class ClienteList(LoginRequiredMixin, ListView):
    model = Clientes
    
class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Clientes
    fields = ['nombre', 'apellido', 'correo']
    success_url =  reverse_lazy('clientes')
    
class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Clientes
    fields = ['nombre', 'apellido', 'correo']
    success_url =  reverse_lazy('clientes')
    
class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Clientes
    success_url =  reverse_lazy('clientes')

class ClienteDetail(LoginRequiredMixin, DetailView):
    model = Clientes
    template_name = 'tiendaapp/clienteDetail.html'
#_________________________________Categoria_____________Class Based Views

class CategoriaList(LoginRequiredMixin, ListView):
    model = Categoria
    
class CategoriaCreate(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = ['nombre', 'articulo']
    success_url =  reverse_lazy('categoria')
    
class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = Categoria
    fields = ['nombre', 'articulo']
    success_url =  reverse_lazy('categoria')
    
class CategoriaDelete(LoginRequiredMixin, DeleteView):
    model = Categoria
    success_url =  reverse_lazy('categoria')

    
#_________________________________________Login / Logout / Registación __________________________________________________________________


def login_request(request):
    if request.method == "POST":
        miForm =AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar
                return render(request, 'tiendaapp/base.html', {'mensaje': f'Bienvenido a nuestro sitio'})  
            else:
                return render(request, 'tiendaapp/login.html', {'form': miForm, 'mensaje': f'Los datos son invalidos'})    
        else:
            return render(request, 'tiendaapp/login.html', {'form': miForm, 'mensaje': f'Los datos son invalidos'}) 
    
    miForm = AuthenticationForm()
    
    return render(request, 'tiendaapp/login.html', {'form': miForm})    



def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "tiendaapp/base.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "tiendaapp/registro.html", {"form":miForm})      

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, 'tiendaapp/base.html')
    
        else:
            return render(request, 'tiendaapp/editarPerfil.html', {'form': form, 'usuario': usuario.username })
        
    else:
        form = UserEditForm(instance=usuario) 
    return render(request, 'tiendaapp/editarPerfil.html', {'form': form, 'usuario': usuario.username })


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            #______Borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            
            #________Guardar el nuevo           
            avatar = Avatar(user=u, imagen=form.cleaned_data["imagen"])
            avatar.save()
            
            #____Hago que la url de la imagen viaje en el request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen
            return render(request,'tiendaapp/base.html')
        
    else:
        form = AvatarFormulario()
    return render(request, 'tiendaapp/agregarAvatar.html', {'form': form})



    
    