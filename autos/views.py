# autos/views.py

from django.shortcuts import render, redirect
from .models import Marca, Auto
from .forms import MarcaForm, AutoForm

def index(request):
    marcas = Marca.objects.all()
    autos = Auto.objects.all()
    return render(request, 'autos/index.html', {'marcas': marcas, 'autos': autos})

def crear_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MarcaForm()
    return render(request, 'autos/crear_marca.html', {'form': form})

def crear_auto(request):
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AutoForm()
    return render(request, 'autos/crear_auto.html', {'form': form})


