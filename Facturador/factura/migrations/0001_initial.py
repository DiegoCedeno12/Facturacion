# Generated by Django 4.1.4 on 2023-02-26 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_type', models.IntegerField(choices=[('01', 'Factura'), ('03', 'Liquidacion de Compra de Bienes y Prestación de Servicios'), ('04', 'Nota de Crédito'), ('05', 'Nota de Débito'), ('06', 'Guía de Remisión'), ('07', 'Comprobante de Retención')], default=1, verbose_name='Tipo de Comprobante')),
                ('Broadcast_date', models.DateField(verbose_name='Fecha de Emision')),
                ('environment_type', models.IntegerField(choices=[(1, 'Pruebas'), (2, 'Produccion')], default=1, verbose_name='Tipo de Ambiente')),
                ('series', models.CharField(max_length=100, verbose_name='Serie')),
                ('voucher_number', models.CharField(max_length=100, verbose_name='Numero de Comprobante')),
                ('numeric_code', models.CharField(max_length=100, verbose_name='Codigo Numerico')),
                ('emission_type', models.IntegerField(choices=[(1, 'Normal')], default=1, verbose_name='Tipo de Emisión')),
                ('Check_digit', models.CharField(max_length=100, verbose_name='Digito Verificador')),
                ('client_identification', models.CharField(max_length=100, verbose_name='Identificación')),
                ('client_social_reason', models.CharField(max_length=150, verbose_name='Razón Social')),
                ('email_customer', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
                ('customer_phone', models.CharField(max_length=100, verbose_name='Telefono')),
                ('customer_address', models.CharField(max_length=150, verbose_name='Dirección')),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.profile', verbose_name='Dueño')),
            ],
            options={
                'verbose_name': 'factura',
                'verbose_name_plural': 'facturas',
                'db_table': 'invoice',
            },
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Precio Unitario')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Subtotal')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='factura.invoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.product', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'item de factura',
                'verbose_name_plural': 'items de factura',
                'db_table': 'invoice_item',
            },
        ),
    ]