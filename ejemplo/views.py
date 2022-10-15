from django.shortcuts import render
from ejemplo.models import Familiar

# Create your views here.
def index(request):
    return render(request, "ejemplo/saludar.html")


def index_dos(request, nombre, apellido):
    return render(request, 'ejemplo/saludar.html',
    {
        'nombre': nombre,
        'apellido': apellido,

    })

def index_tres(request):
    return render(request, 'ejemplo/saludar.html',
    {'notas':[1,2,3,4,5,6,7,8]})

def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})