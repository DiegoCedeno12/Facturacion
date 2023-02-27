from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from .forms import AuthenticationForm, businessForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.models import Group

# Create your views here.
@csrf_exempt
def login(request):
    data = {
        'user': AuthenticationForm()
    }
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(username = form.cleaned_data["username"], password =form.cleaned_data["password"])
            messages.success(request, "Bienvenido "+user.get_username())
            auth.login(request, user)
            return redirect(to="home")
        data["user"] = form
    
    return render(request, 'usuario/login.html', data)

@csrf_exempt
def business(request, id):
    usuario = get_object_or_404(Profile, user = id)
    data = {
        'business': businessForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = businessForm(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'El Perfil de {usuario.user.username.upper()} se modificó con exito')
            return redirect(to="home")
        else:
            print('Falló')
            data["business"] = formulario

    return render(request, 'usuario/business.html', data)
