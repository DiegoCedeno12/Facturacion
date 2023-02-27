from django.db import models

# Create your models here.
class Provider(models.Model):
    identify = models.IntegerField(verbose_name="Identificación", unique=True)
    name = models.CharField(max_length=150, verbose_name="Nombre")
    cellPhone = models.CharField(max_length=10, verbose_name="Telefono/Celular")
    email = models.EmailField(verbose_name="Correo Electronico")
    addres = models.CharField(verbose_name="Dirección", max_length=250)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'