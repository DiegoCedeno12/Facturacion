"""Facturador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from core import views as coreViews
from usuario import views as usuarioViews
from proveedor import views as proveedoresViews
from producto import views as productosViews
#from clientes import views as clienteviews
from factura import views as factura_views
from django.conf import settings

urlpatterns = [
    path('', coreViews.home, name="home"),
    path('admin/', admin.site.urls),

#----------------------------------- Users ------------------------------------------------------
    path('login/', usuarioViews.login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/<int:id>', usuarioViews.business, name="business"),

#----------------------------------- Proveedores ------------------------------------------------------
    path('provider/', proveedoresViews.provider, name='provider'),
    path('provider/add/', proveedoresViews.addProvider, name='addProvider'),
    path('provider/modify/', proveedoresViews.modifyProvider, name='modifyProvider'),
    path('provider/delete/<id>/', proveedoresViews.deleteProvider, name='deleteProvider'),

#----------------------------------- Productos ------------------------------------------------------
    path('product/', productosViews.product, name='product'),
    path('product/add/', productosViews.addProduct, name='addProduct'),
    path('product/modify/', productosViews.modifyProduct, name='modifyProduct'),
    #path('productProvider/', productosViews.product, name='productProvider'),
    path('product/delete/<id>/', productosViews.deleteProduct, name='deleteProduct'),

#---------------------------------- Clientes ----------------------------------------------------
    #path('customer/add/', clienteviews.addCustomer, name='addCustomer'),
    #path('customer/', clienteviews.customer, name='customer'),
    #path('customer/modify/', clienteviews.modifyCustomer, name="modifyCustomer"),
    #path('customer/delete/<id>/', clienteviews.deleteCustomer, name="deleteCustomer"),

#---------------------------------- Factura ----------------------------------------------------
    path('invoice/', factura_views.invoice, name='invoice'),
    path('invoice/add/', factura_views.addInvoice, name='addInvoice'),
    path('invoice/delete/<id>/', factura_views.deleteInvoice, name='delInvoice'),
    path('get_product_price/', factura_views.get_product_price, name="get_product_price"),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)