from django.db import models
#from django.contrib.auth import User 

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    articulo = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}, {self.articulo}"
    

class Productos(models.Model):  
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10,decimal_places=3)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre}, {self.categoria}, {self.precio}"
 
class Clientes(models.Model): 
    nombre = models.CharField(max_length=100, blank=False)
    apellido = models.CharField(max_length=100, blank=False)
    correo = models.EmailField(blank=False)
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.correo}"
    
    #______________________________________________________
    
    #Imagenes
    #class Avatar(models.Model):
        imagen = models.ImageField(upload_to="avatares")
        user = models.ForeignKey(User)
        
        def __str__(self):
            return f"{self.user} {self.imagen}"