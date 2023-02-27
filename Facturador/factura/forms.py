from django import forms
from factura.models import Invoice
from producto.models import Product


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

class invoiceForm (forms.ModelForm):

    voucher_type = forms.IntegerField(
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'inputTipoComprobantes'
            }, choices=typeVoucher
        )
    )

    Broadcast_date = forms.DateField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "date",
                'id': "FechaEmision",
                'readonly': True
            }
        )
    )

    environment_type = forms.IntegerField(
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'inputTipoAmbiente'
            }, choices=typeambiente
        )
    )

    series = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "inputSerie"
            }
        )
    )

    voucher_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "inputNumComprobante"
            }
        )
    )

    numeric_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "inputCodigoNumerico"
            }
        )
    )

    emission_type = forms.IntegerField(
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'inputTipoEmision'
            }, choices=typeEmision
        )
    )

    Check_digit = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "inputDigitoVerificador",
                'readonly': True
            }
        )
    )

    client_identification = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "identificacion"
            }
        )
    )

    client_social_reason = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "nombresApellidos"
            }
        )
    )

    email_customer = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "email",
                'id': "coreoElectronico"
            }
        )
    )

    customer_phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "Telefono"
            }
        )
    )

    customer_address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "Direccion"
            }
        )
    )

    products = forms.IntegerField(widget=forms.Select(
            attrs={
                'class':"form-select js-example-basic-multiple", 'name':"states[]", 'multiple':"multiple", 'id':'productoseleccionado'
            }, choices=Product.objects.values_list('id', 'name')
        ))
    
    total_amount = forms.DecimalField(required=False,
        widget=forms.TextInput(
        attrs={
        'step' : "0.01" ,
        'class': 'form-control',
        'type': 'number',
        'value':''
        
        })
    )

    class Meta:
        model = Invoice
        fields = ['total_amount','products', 'owner', 'voucher_type', 'Broadcast_date', 'environment_type', 'series', 'voucher_number', 'numeric_code',
                  'emission_type', 'Check_digit', 'client_identification', 'client_social_reason', 'email_customer', 'customer_phone', 'customer_address']


from django.forms import inlineformset_factory
from .models import Invoice, InvoiceItem, Product

class InvoiceForm(forms.ModelForm):

    voucher_type = forms.IntegerField(
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'inputTipoComprobantes'
            }, choices=typeVoucher
        )
    )

    Broadcast_date = forms.DateField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "date",
                'id': "FechaEmision",
                'readonly': True
            }
        )
    )

    environment_type = forms.IntegerField(
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'inputTipoAmbiente'
            }, choices=typeambiente
        )
    )

    series = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "inputSerie"
            }
        )
    )

    voucher_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "inputNumComprobante"
            }
        )
    )

    numeric_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "inputCodigoNumerico"
            }
        )
    )

    emission_type = forms.IntegerField(
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'inputTipoEmision'
            }, choices=typeEmision
        )
    )

    Check_digit = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "inputDigitoVerificador",
                'readonly': True
            }
        )
    )

    client_identification = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "identificacion"
            }
        )
    )

    client_social_reason = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "nombresApellidos"
            }
        )
    )

    email_customer = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "email",
                'id': "coreoElectronico"
            }
        )
    )

    customer_phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "Telefono"
            }
        )
    )

    customer_address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text",
                'id': "Direccion"
            }
        )
    )

    class Meta:
        model = Invoice
        fields = ('voucher_type', 'Broadcast_date', 'environment_type', 'series', 'voucher_number', 'numeric_code', 'emission_type', 'Check_digit', 'client_identification', 'client_social_reason', 'email_customer', 'customer_phone', 'customer_address')

class InvoiceItemForm(forms.ModelForm):

    class Meta:
        model = InvoiceItem
        fields = ('product', 'quantity', 'unit_price', 'subtotal')
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control invoice-product'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'unit_price': forms.TextInput(attrs={'class': 'form-control', 'step':"0.01", 'type': 'number','readonly': True}),
            'subtotal': forms.TextInput(attrs={'class': 'form-control', 'step':"0.01", 'type': 'number','readonly': True})
        }

InvoiceItemFormSet = inlineformset_factory(Invoice, InvoiceItem, form=InvoiceItemForm, extra=1)
