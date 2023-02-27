from django import forms
from .models import Product

class providerSelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        return option

class ProductForm(forms.ModelForm):
        
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['provider'].label = "Proveedores:"

    vat_rate = [
        [1, '0%'],
        [2, '12%'],
        [3, '14%'],
        [4, 'No Objeto de Impuesto'],
        [5, 'Exento de IVA']
    ]

    master_code = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "number",
                'id' : 'codigoPrincipal'
            }
        ), label='Codigo Principal:'
    )

    auxiliary_code = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "number",
                'id' : "codigoAuxiliar"
            }
        ),label="Codigo Auxiliar:"
    )

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "NombreEdit"
            }
        ),label="Nombre de Producto:"
    )

    stock = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "number",
                'id' : "stock"
            }
        ),label="Stock/Cantidad:"
    )

    unit_price = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                'step' : "0.01" ,
                'class': 'form-control',
                'type' : "number",
                'id' : "precioUnitario"
            }
        ),label="Precio Unitario:"
    )

    vat_rate = forms.IntegerField(
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id' : 'valorIva'
            },
            choices=vat_rate,
        ),label="IVA:"
    )
    
    class Meta:

        model = Product
        fields = ['provider', 'master_code', 'auxiliary_code', 'name', 'stock', 'unit_price', 'vat_rate']
        widgets = { 'provider': providerSelect(
            attrs={
            'class': 'form-select'
            }
        )}

class editProductForm(forms.ModelForm):

    vat_rate = [
        [1, '0%'],
        [2, '12%'],
        [3, '14%'],
        [4, 'No Objeto de Impuesto'],
        [5, 'Exento de IVA']
    ]

    master_code = forms.IntegerField(disabled=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "number",
                'id' : 'codigoPrincipalEdit'
            }
        ), label='Codigo Principal:'
    )

    auxiliary_code = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "number",
                'id' : "codigoAuxiliarEdit"
            }
        ),label="Codigo Auxiliar:"
    )

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "NombreEdit"
            }
        ),label="Nombre de Producto:"
    )

    stock = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "number",
                'id' : "stockEdit"
            }
        ),label="Stock/Cantidad:"
    )

    unit_price = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                'step' : "0.01" ,
                'class': 'form-control',
                'type' : "number",
                'id' : "precioUnitarioEdit"
            }
        ),label="Precio Unitario:"
    )

    vat_rate = forms.IntegerField(
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id' : 'valorIvaEdit'
            },
            choices=vat_rate,
        ),label="IVA:"
    )
    
    class Meta:

        model = Product
        exclude = ['provider']
        fields = ['master_code', 'auxiliary_code', 'name', 'stock', 'unit_price', 'vat_rate']