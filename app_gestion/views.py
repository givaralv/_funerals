
from django.shortcuts import render, redirect
from .forms import ContactoForm

from .models import Obituario, DetalleObituario, Blog
from .forms import ObituarioForm, DetalleObituarioForm, CondolenciaForm


# Create your views here.

def inicio(request):
    return render(request,"inicio.html")


def contacto(request):
    
    data= {
        'form': ContactoForm(),
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Contacto enviado Correctamente"
        else:
            data['form'] = formulario

    return render(request, "contacto.html", data)


def crear_obituario(request):
    if request.method == 'POST':
        obituario_form = ObituarioForm(request.POST, request.FILES)
        detalle_form = DetalleObituarioForm(request.POST)
        if obituario_form.is_valid() and detalle_form.is_valid():
            obituario = obituario_form.save()
            detalle = detalle_form.save(commit=False)
            detalle.obituario = obituario
            detalle.save()
            return redirect('listar_obituarios')
    else:
        obituario_form = ObituarioForm()
        detalle_form = DetalleObituarioForm()
    return render(request, 'obituarios/crear.html', {
        'obituario_form': obituario_form,
        'detalle_form': detalle_form
    })


def listar_obituarios(request):
    obituarios = Obituario.objects.all()
    return render(request, 'obituarios/listar.html', {'obituarios': obituarios})


def ver_obituario(request, id):
    obituario = Obituario.objects.get(pk=id)
    try:
        detalle = obituario.detalleobituario
    except DetalleObituario.DoesNotExist:
        detalle = None
    return render(request, 'obituarios/infAdicional.html', {
        'obituario': obituario,
        'detalle': detalle
    })


def nosotros(request):
    return render(request, 'nosotros.html')


def ver_obituario(request, id):
    obituario = Obituario.objects.get(pk=id)
    try:
        detalle = obituario.detalleobituario
    except DetalleObituario.DoesNotExist:
        detalle = None

    # Manejo de envío de condolencias
    if request.method == 'POST':
        condolencia_form = CondolenciaForm(request.POST)
        if condolencia_form.is_valid():
            nueva_condolencia = condolencia_form.save(commit=False)
            nueva_condolencia.obituario = obituario
            nueva_condolencia.save()
            return redirect('ver_obituario', id=obituario.id)
    else:
        condolencia_form = CondolenciaForm()

    condolencias = obituario.condolencias.all().order_by('-fecha_envio')

    return render(request, 'obituarios/infAdicional.html', {
        'obituario': obituario,
        'detalle': detalle,
        'condolencia_form': condolencia_form,
        'condolencias': condolencias
    })

def blog_list(request):
    blogs = Blog.objects.all().order_by('-fecha_publicacion')
    return render(request, 'blog.html', {'blogs': blogs})
