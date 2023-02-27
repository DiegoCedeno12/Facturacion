from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile

class AuthenticationForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "username",
                'placeholder' : "Nombre Usuario"
            }
        )
    )

    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "password",
                'id' : "password",
                'placeholder' : "Contraseña"
            }
        )
    )

    class Meta:
        model = User
        fields = ["username", "password"]

class businessForm(forms.ModelForm):

    typecontabilidad = [
        [1, 'No'],
        [2, 'Si']
    ]

    ruc = forms.IntegerField(
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "number",
                'id' : "ruc"
            }
        )
    )
    businessName = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "razonSocial"
            }
        )
    )
    tradename = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "nombreComercial"
            }
        )
    )

    establishmentAddress  = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "direccionEstablecimiento"
            }
        )
    )

    senderAddress = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "direccionEmisor"
            }
        )
    )
    
    IssuerCode = forms.IntegerField(
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "number",
                'id' : "codigoEmisor"
            }
        )
    )
    
    EmissionPoint = forms.IntegerField(
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "number",
                'id' : "puntoEmision"
            }
        )
    )
  
    SpecialTaxpayer = forms.IntegerField(
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "number",
                'id' : "contribuyenteEspecial"
            }
        )
    )

    Accounting = forms.IntegerField(
        widget= forms.Select(
            attrs={
                'class': 'form-select',
                'id' : 'llevarContabilidad'
            }, choices= typecontabilidad
        )
    )

    Logo = forms.FileField(
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "file",
                'id' : "logoEmpresa"
            }
        )
    )

    ElectronicSignature = forms.FileField(
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "file",
                'id' : "firmaElectronica"
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        # asi vuelves tus campos no requeridos
        self.fields['ruc'].required = False
        self.fields['businessName'].required = False
        self.fields['tradename'].required = False
        self.fields['establishmentAddress'].required = False
        self.fields['senderAddress'].required = False
        self.fields['IssuerCode'].required = False
        self.fields['EmissionPoint'].required = False
        self.fields['SpecialTaxpayer'].required = False
        self.fields['Accounting'].required = False
        self.fields['Logo'].required = False
        self.fields['ElectronicSignature'].required = False

    class Meta:
        model = Profile
        #exclude = ['user']
        fields = ['ruc', 'businessName', 'tradename', 'establishmentAddress', 'senderAddress', 'Accounting', 'IssuerCode', 'EmissionPoint', 'SpecialTaxpayer', 'Logo', 'ElectronicSignature']
