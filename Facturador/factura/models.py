from django.db import models
from usuario.models import Profile
from producto.models import Product
import xml.etree.ElementTree as ET
from django.core.files.base import ContentFile

# Create your models here.
typeVoucher = [
    (1, 'Factura'),
    (3, 'Liquidacion de Compra de Bienes y Prestación de Servicios'),
    (4, 'Nota de Crédito'),
    (5, 'Nota de Débito'),
    (6, 'Guía de Remisión'),
    (7, 'Comprobante de Retención')
]

typeEmision = [
    (1, 'Normal')
]

typeambiente = [
    (1, 'Pruebas'),
    (2, 'Produccion')
]

class Invoice(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Dueño')
    voucher_type = models.IntegerField(choices=typeVoucher, default=1, verbose_name='Tipo de Comprobante')
    Broadcast_date = models.DateField(verbose_name='Fecha de Emision' )
    environment_type = models.IntegerField(choices=typeambiente, default=1, verbose_name='Tipo de Ambiente' )
    series = models.CharField(max_length=100, verbose_name='Serie' )
    voucher_number = models.CharField(max_length=100, verbose_name='Numero de Comprobante' )
    numeric_code = models.CharField(max_length=100, verbose_name='Codigo Numerico')
    emission_type = models.IntegerField(choices=typeEmision, default=1, verbose_name='Tipo de Emisión' )
    Check_digit = models.CharField(max_length=100, verbose_name='Digito Verificador' )
    client_identification = models.CharField(max_length=100, verbose_name='Identificación' )
    client_social_reason = models.CharField(max_length=150, verbose_name='Razón Social' )
    email_customer = models.EmailField(verbose_name='Correo Electronico' )
    customer_phone = models.CharField(max_length=100, verbose_name='Telefono' )
    customer_address = models.CharField(max_length=150, verbose_name='Dirección' )
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Total', blank=True, null=True)
    xml_file = models.FileField(upload_to='invoices/xml/', blank=True, null=True, verbose_name='Archivo XML')
    
    class Meta:
        db_table = 'invoice'
        verbose_name = 'factura'
        verbose_name_plural = 'facturas'

    def __str__(self):
        return f'{self.voucher_number} | {self.client_identification}'
    
    def create_xml_file(self):
        # Crear el XML de la factura
        invoice_xml = ET.Element('Factura')
        ET.SubElement(invoice_xml, 'Fast_Fact').text = str(self.owner)
        ET.SubElement(invoice_xml, 'Total').text = str(self.total_amount)
        print("Para identificarlo: ", self.voucher_type)
        # Agregar información de factura
        factura_xml = ET.SubElement(invoice_xml, 'infoTributaria')
        ET.SubElement(factura_xml, 'tipoComprobante').text = str(self.voucher_type)
        ET.SubElement(factura_xml, 'ruc').text = str(self.owner.ruc)
        ET.SubElement(factura_xml, 'fechaEmision').text = str(self.Broadcast_date)
        ET.SubElement(factura_xml, 'ambiente').text = str(self.environment_type)
        ET.SubElement(factura_xml, 'secuencial').text = str(self.series)
        ET.SubElement(factura_xml, 'ptoEmi').text = str(self.voucher_number)
        ET.SubElement(factura_xml, 'codigoNumerico').text = str(self.numeric_code)
        ET.SubElement(factura_xml, 'tipoEmision').text = str(self.emission_type)
        ET.SubElement(factura_xml, 'claveAcceso').text = str(self.Check_digit)

        # Agregar información del cliente
        cliente_xml = ET.SubElement(invoice_xml, 'cliente')
        ET.SubElement(cliente_xml, 'identificacionComprador').text = str(self.client_identification)
        ET.SubElement(cliente_xml, 'razonSocialComprador').text = str(self.client_social_reason)

        for item in self.items.all():
            item_xml = ET.SubElement(invoice_xml, 'Productos')
            ET.SubElement(item_xml, 'descripcion').text = str(item.product)
            ET.SubElement(item_xml, 'cantidad').text = str(item.quantity)
            ET.SubElement(item_xml, 'precioUnitario').text = str(item.unit_price)
            ET.SubElement(item_xml, 'precioTotalSinImpuesto').text = str(item.subtotal)

        # Guardar el XML de la factura en un archivo en memoria
        xml_string = ET.tostring(invoice_xml, encoding='utf-8')
        xml_file = ContentFile(xml_string)
        xml_file.name = f'{self.Check_digit}.xml'
        self.xml_file = xml_file
        self.save()


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    quantity = models.PositiveIntegerField(verbose_name='Cantidad')
    unit_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Precio Unitario')
    subtotal = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Subtotal')

    class Meta:
        db_table = 'invoice_item'
        verbose_name = 'item de factura'
        verbose_name_plural = 'items de factura'

    def __str__(self):
        return f'{self.product} ({self.quantity})'