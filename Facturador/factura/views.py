from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Invoice
from usuario.models import Profile
from producto.models import Product
from .forms import InvoiceForm, InvoiceItemFormSet
import os

# Create your views here.
@login_required
def invoice(request):
    facturas = Invoice.objects.all()
    data = {
        'factura' : facturas
    }
    return render(request, "factura/invoice.html", data)

def addInvoice(request):
    # Obtener los productos disponibles
    productos = Product.objects.all()
    duenio = get_object_or_404(Profile, pk=request.user.id)

    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        formset = InvoiceItemFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            
            # Guardar la factura en la base de datos
            invoice = form.save(commit=False)
            invoice.owner = request.user.profile
            invoice.total_amount = 0
            invoice.save()

            # Calcular el total de la factura
            total = 0
            for formu in formset:
                if formu.cleaned_data.get('product'):
                    item = formu.save(commit=False)
                    item.invoice = invoice
                    item.subtotal = item.quantity * item.unit_price
                    item.save()
                    total += item.subtotal

            # Actualizar el total de la factura
            invoice.total_amount = total
            invoice.save()

            # Crear el XML de la factura
            # Guardar el XML de la factura en un archivo en memoria
            invoice.create_xml_file()

            return redirect(to='invoice')

    else:
        print('Falló')
        form = InvoiceForm()
        formset = InvoiceItemFormSet()

    return render(request, 'factura/addInvoice.html', {'duenio': duenio,'productos': productos, 'form': form, 'formset': formset})

from django.http import JsonResponse

def get_product_price(request):
    product_id = request.GET.get('product_id')
    print(product_id)
    product = Product.objects.get(pk=product_id)
    return JsonResponse({'price': product.unit_price})

def deleteInvoice(request, id):
    factura = get_object_or_404(Invoice, pk=id)
    if factura.xml_file:
        if os.path.isfile(factura.xml_file.path):
            os.remove(factura.xml_file.path)
    factura.delete()
    return redirect(to='invoice')