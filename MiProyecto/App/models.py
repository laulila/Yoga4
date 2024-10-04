from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre_usuario = models.CharField(max_length=30)
    email_usuario = models.EmailField()
    
    def __str__(self):
        return f'Nombre_usuario: {self.nombre_usuario}, Email_usuario: {self.email_usuario}'
    
class Productos(models.Model):
    nombre_producto = models.CharField(max_length=30)
    marca_producto = models.CharField(max_length=20)
    
    def __str__(self):
        return f'Nombre_producto: {self.nombre_producto}, Marca_Producto: {self.marca_producto}'
    
class Ventas_detalles(models.Model):
    monto = models.FloatField()
    fecha_venta = models.DateField()
    forma_de_pago = models.CharField(max_length=25)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Monto: {self.monto}, Fecha_venta: {self.fecha_venta}, Forma_de_pago: {self.forma_de_pago}, producto: {self.producto}, usuario: {self.usuario}'
    
    
