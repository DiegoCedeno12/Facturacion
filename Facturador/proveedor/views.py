from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Provider
from .forms import editProviderForm, ProviderForm

# Create your views here.
@login_required
def provider(request):
    provider = Provider.objects.all()
    editProvider = editProviderForm()

    data = {
        'Provider' : provider,
        'editProvider' : editProvider
    }
    return render(request, "proveedor/provider.html", data)

@login_required
def addProvider(request):
    data = {
        'addProvider' : ProviderForm()
    }
    if request.method == 'POST':
        formulario = ProviderForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'Se agregó un nuevo Proveedor')
            return redirect(to="provider")
        else:
            data["addProvider"] = formulario
    return render(request, "proveedor/addProvider.html", data)

@login_required
def modifyProvider(request):
    provider = Provider.objects.get(pk=request.POST.get("id_provider_editar"))
    formulario = editProviderForm(
        request.POST, instance=provider
    )
    if formulario.is_valid:
        formulario.save()
        messages.success(request, f'El proveedor {provider.name.upper()} fue modificado')
        return redirect(to="provider")

@login_required
def deleteProvider(request, id):
    provider = get_object_or_404(Provider, id=id)
    provider.delete()
    messages.success(request, f"El proveedor {provider.name.upper()} fue eliminado")
    return redirect(to="provider")