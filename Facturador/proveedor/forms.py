from django import forms
from .models import Provider

class ProviderForm(forms.ModelForm):
    identify = forms.IntegerField(
        widget= forms.TextInput(
            attrs={
                'class' : 'form-control',
                'type' : "number",
                'id' : 'Identificacion'
            }
        )
    )

    name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class' : 'form-control',
                'type' : "text",
                'id' : 'Nombre'
            }
        )
    )

    cellPhone = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class' : 'form-control',
                'type' : "text",
                'id' : 'Telefono'
            }
        )
    )

    email = forms.EmailField(
        widget= forms.TextInput(
            attrs={
                'class' : 'form-control',
                'type' : "email",
                'id' : 'Correo'
            }
        )
    )

    addres = forms.CharField(
        widget= forms.Textarea(
            attrs={
                'class' : 'form-control',
                'type' : "text",
                'id' : 'Direccion',
                'rows' : '2'
            }
        )
    )

    class Meta:
        model = Provider
        fields = ["identify", "name", "cellPhone", "email", "addres"]

class editProviderForm(forms.ModelForm):
    identify = forms.IntegerField(
        widget= forms.TextInput(
            attrs={
                'class' : 'form-control',
                'type' : "number",
                'id' : 'identificacionEdit'
            }
        ), label='Identificación:'
    )

    name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class' : 'form-control',
                'type' : "text",
                'id' : 'nombreEdit'
            }
        ), label='Nombre:'
    )

    cellPhone = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class' : 'form-control',
                'type' : "text",
                'id' : 'telefonoEdit'
            }
        ), label='Telefono/Celular:'
    )

    email = forms.EmailField(
        widget= forms.TextInput(
            attrs={
                'class' : 'form-control',
                'type' : "email",
                'id' : 'correoEdit'
            }
        ), label='Correo Electrónico:'
    )

    addres = forms.CharField(
        widget= forms.Textarea(
            attrs={
                'class' : 'form-control',
                'type' : "text",
                'id' : 'direccionEdit',
                'rows' : '2'
            }
        ), label='Dirección:'
    )

    class Meta:
        model = Provider
        fields = ['id', "identify", "name", "cellPhone", "email", "addres"]