from django.db import models
from django.contrib.auth.models import User

# Create your models here.
typecontabilidad = [
    [1, 'No'],
    [2, 'Si']
]

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ruc = models.IntegerField(blank=True, verbose_name="Numero de Ruc", null=True)
    businessName = models.CharField(max_length=150, blank=True, verbose_name="Razon Social", null=True)
    tradename = models.CharField(max_length=150, blank=True, verbose_name="Nombre Comercial", null=True)
    establishmentAddress  = models.CharField(max_length=150, blank=True, verbose_name="direccion establecimiento", null=True)
    senderAddress = models.CharField(max_length=150, blank=True, verbose_name="direccion emisor", null=True)
    IssuerCode = models.IntegerField(blank=True, verbose_name="Codigo Emisor", null=True)
    EmissionPoint = models.IntegerField(blank=True, verbose_name="Punto Emisión", null=True)
    SpecialTaxpayer = models.IntegerField(blank=True, verbose_name="Contribuyente Especial", null=True)
    Accounting = models.IntegerField(verbose_name="Contabilidad", choices=typecontabilidad, default=1)
    Logo = models.FileField(verbose_name="Logotipo de la Empresa",blank=True,null=True, upload_to='logo')
    ElectronicSignature = models.FileField(verbose_name="Firma electronica",blank=True,null=True)

    def __str__(self):
        return f"{self.user.first_name}"

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'