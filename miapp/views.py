from django.shortcuts import render , HttpResponse, redirect
from miapp.models import Region
from django.db.models import Q
from miapp.forms import FormRegion
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def regiones(request):
    
    
    regiones = Region.objects.all()

    return render(request, 'regiones.html',{
        'regiones': regiones,
        'titulo': 'Listado de Regiones'
    })

def crear_region(request):
    if request.method == 'POST':
        formulario = FormRegion(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            name = data_form.get('name')
            cases = data_form['cases']
            deaths = data_form['deaths']
            lethality = data_form['lethality']
            
            region = Region(
                name = name,
                cases = cases,
                deaths = deaths,
                lethality = lethality
            )
            region.save()

            #Es para crear un mensaje Flash (Solo se muestra una vez)
            messages.success(request,f'Se agregó correctamente la region {region.id}')

            return redirect('region')
            #return HttpResponse(articulo.titulo + ' - ' + articulo.contenido + ' - ' + str(articulo.publicado))
    else:
        formulario = FormRegion()        
    return render(request, 'crear_region.html',{
        'form': formulario
    })

def empleados(request):
    return render(request,'empleados.html')

def crear_empleado(request):
    return render(request,'crear_empleado.html')