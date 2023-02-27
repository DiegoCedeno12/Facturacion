from django.db import models
from proveedor.models import Provider

# Create your models here.
vat_rate = [
    [1, '0%'],
    [2, '12%'],
    [3, '14%'],
    [4, 'No Objeto de Impuesto'],
    [5, 'Exento de IVA']
]

class Product(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, verbose_name='Proveedor')
    master_code = models.IntegerField(unique=True ,verbose_name='Codigo Principal')
    auxiliary_code = models.IntegerField(unique=True ,verbose_name='Codigo Auxiliar')
    name = models.CharField(max_length=100, verbose_name='Nombre Producto')
    stock = models.IntegerField(verbose_name="Cantidad")
    unit_price = models.DecimalField(max_digits=15, decimal_places=2 , verbose_name='Precio Unitario')
    vat_rate = models.IntegerField(choices=vat_rate, default=1, verbose_name='Tipo de IVA')

    class Meta:
        db_table = 'product'
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return f'{self.name}'