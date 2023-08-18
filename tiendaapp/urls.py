
from django.urls import include, path
from .views import *

urlpatterns = [
   path('', home, name='home'),
   path('categoria/', categoria, name='categoria'),
   path('productos/', productos, name='productos'),
   path('clientes/', clientes, name='clientes'),
   
   #path('producto_form/', productoForm, name='producto_form'),
   
   
   path('producto_form/', productoForm, name='producto_form'),
   path('categoria_form/', categoriaForm, name='categoria_form'),
   path('cliente_form/', clienteForm, name='cliente_form'),
   
   path('buscar_categoria/', buscarCategoria, name='buscar_categoria'),
   path('buscar_categoria2/', buscarCategoria2, name='buscar_categoria2'),
   
   
   path('buscar_producto/', buscarProducto, name='buscar_producto'),
   path('buscar_producto2/', buscarProducto2, name='buscar_producto2'),
   
   path('buscar_cliente/', buscarCliente, name='buscar_cliente'),
   path('buscar_cliente2/', buscarCliente2, name='buscar_cliente2'),
   

   path('agregar_producto/', agregarProducto, name='agregar_producto'),
   path('agregar_cliente/', agregarCliente, name='agregar_cliente'),
   path('agregar_categoria/', agregarCategoria, name='agregar_categoria'),
   
   
   
]
