from django.http import HttpResponse
from django.shortcuts import  redirect, render
from .models import Productos , Categoria , Clientes
from .forms import *
# Create your views here.


def home(request):
    return render(request, 'tiendaapp/home.html')

def categoria(request):
    contexto = {'categoria': Categoria.objects.all(),'titulo': 'Categoria de Productos'}
    return render(request, 'tiendaapp/categoria.html', contexto)

def productos(request):
    contexto = {'productos': Productos.objects.all(),'titulo': 'Lista de Productos en Stock'}
    return render(request, 'tiendaapp/productos.html', contexto)

def clientes(request):
    contexto = {'clientes': Clientes.objects.all(),'titulo': 'Listado de Clientes Registrados'}
    return render(request, 'tiendaapp/clientes.html', contexto)



 #__________________________________________________________#

 
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


def buscarCategoria(request):
    return render(request, "tiendaapp/buscarCategoria.html")


def buscarCategoria2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        categoria = Categoria.objects.filter(nombre__icontains=patron)
        contexto = {"categoria": categoria, 'titulo': f'La categoria que tienen como patron "{patron}"'}
        return render(request, "tiendaapp/categoria.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")

#_____________________________________________________________________________________

    
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



def buscarProducto(request):
    return render(request, "tiendaapp/buscarProducto.html")


def buscarProducto2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        producto = Productos.objects.filter(nombre__icontains=patron)
        contexto = {"productos": producto, 'titulo': f'Lista de Productos que tienen como patron "{patron}"'}
        return render(request, "tiendaapp/productos.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")

#_____________________________________________________________________________________

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


def buscarCliente(request):
    return render(request, "tiendaapp/buscarCliente.html")


def buscarCliente2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        cliente = Clientes.objects.filter(nombre__icontains=patron)
        contexto = {"clientes": cliente, 'titulo': f'Lista de Clientes que tienen como patron "{patron}"'}
        return render(request, "tiendaapp/clientes.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")



#______________________________________________________________________________________________________________




def agregarProducto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect ( "productos")
        
        
    else:
            producto_form = ProductoForm()
            
    return render(request,'tiendaapp/formularioProducto.html', {'producto_form':producto_form})
            
    
    
def agregarCliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect ( "clientes")
       
    else:
            cliente_form = ClienteForm()
            
    return render(request,'tiendaapp/formularioCliente.html', {'cliente_form':cliente_form})
            
    
def agregarCategoria(request):
    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST)
        if categoria_form.is_valid():
            categoria_form.save()
            return redirect ( "categoria")
                 
        
    else:
            categoria_form = CategoriaForm()
            
    return render(request,'tiendaapp/formularioCategoria.html', {'categoria_form':categoria_form})
            
    