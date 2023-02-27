from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from proveedor.models import Provider
from producto.models import Product
from factura.models import Invoice


# Create your views here.
@login_required
def home(request):
    provider = Provider.objects.count
    product = Product.objects.count
    invoice = Invoice.objects.count
    data = {
        'providerCount' : provider,
        'productCount' : product,
        'invoiceCount': invoice
    }
    
    return render(request, "core/home.html", data)