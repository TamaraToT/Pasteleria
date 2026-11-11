from django.db import models


class Linea(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    linea = models.ForeignKey(
        Linea,
        on_delete=models.CASCADE,
        related_name='productos'
    )
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    fotografia = models.ImageField(upload_to='productos/')
    precio = models.PositiveIntegerField()
    porciones = models.PositiveIntegerField()
    apto_celiacos = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


import uuid


class Encargo(models.Model):
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name='encargos'
    )
    nombre_cliente = models.CharField(max_length=150)
    correo = models.EmailField()
    fecha_retiro = models.DateField()
    cantidad = models.PositiveIntegerField()
    fecha_encargo = models.DateTimeField(auto_now_add=True)
    codigo = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    def __str__(self):
        return f"Encargo {self.codigo}"

