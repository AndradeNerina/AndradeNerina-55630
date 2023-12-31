
from django.urls import include, path
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('', home, name='home'),
   path('about/', about_me, name='about'),
   
  
   
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
   
   #_____________________________________________________
  
   
   path('productos/', ProductoList.as_view(), name='productos'),
   path('create_producto/', ProductoCreate.as_view(), name='create_producto'),
   path('update_producto/<int:pk>/', ProductoUpdate.as_view(), name='update_producto'),
   path('delete_producto/<int:pk>/',ProductoDelete.as_view(), name='delete_producto'),
   path('detail_producto/<int:pk>/',ProductoDetail.as_view(), name='detail_producto'),
   
   path('clientes/', ClienteList.as_view(), name='clientes'),
   path('create_cliente/', ClienteCreate.as_view(), name='create_cliente'),
   path('update_cliente/<int:pk>/', ClienteUpdate.as_view(), name='update_cliente'),
   path('delete_cliente/<int:pk>/',ClienteDelete.as_view(), name='delete_cliente'),
   path('detail_cliente/<int:pk>/',ClienteDetail.as_view(), name='detail_cliente'),
   
   path('categoria/', CategoriaList.as_view(), name='categoria'),
   path('create_categoria/', CategoriaCreate.as_view(), name='create_categoria'),
   path('update_categoria/<int:pk>/', CategoriaUpdate.as_view(), name='update_categoria'),
   path('delete_categoria/<int:pk>/',CategoriaDelete.as_view(), name='delete_categoria'),
   
   
   path('login/', login_request, name='login'),
   path('logout/', LogoutView.as_view(template_name="tiendaapp/logout.html"), name='logout'),
   path('registro/', register, name='registro'),
   path('editar_perfil/', editarPerfil, name='editar_perfil'),
   path('agregar_avatar/', agregarAvatar, name='agregar_avatar'),
   
   
    
]
