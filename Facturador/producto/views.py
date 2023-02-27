from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import ProductForm, editProductForm

# Create your views here.

def product(request):
    products = Product.objects.all()
    editProduct = editProductForm()
    data = {
        'Products' : products,
        'editProduct' : editProduct
    }
    return render (request, 'producto/product.html', data)

def addProduct(request):
    data = {
        'addProduct' : ProductForm()
    }
    if request.method == 'POST':
        formulario = ProductForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'Se agregó un nuevo Producto')
            return redirect(to="product")
        else:
            data["addProduct"] = formulario
    return render (request, 'producto/addProduct.html', data)

def modifyProduct(request):
    product = Product.objects.get(pk=request.POST.get("id_product_editar"))
    formulario = editProductForm(
        request.POST, instance=product
    )
    if formulario.is_valid:
        formulario.save()
        messages.success(request, f'El producto {product.name.upper()} fue modificado')
        return redirect(to="product")

def deleteProduct(request, id):
    productos = get_object_or_404(Product, id=id)
    productos.delete()
    messages.success(request, f'El producto {productos.name} fue eliminado')
    return redirect(to="product")
