from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def regiones(request):
    return render(request,'regiones.html')

def crear_region(request):
    return render(request,'crear_region.html')

def empleados(request):
    return render(request,'empleados.html')

def crear_empleado(request):
    return render(request,'crear_empleado.html')