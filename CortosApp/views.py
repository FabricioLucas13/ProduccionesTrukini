from django.shortcuts import render, HttpResponse

# Create your views here.

def cortos(request):
    return render(request,"CortosApp/cortos.html")

def desgracia(request):
    return render(request,"CortosApp/temporadauno/desgracia.html")

def capitulo(request):
    return render(request,"CortosApp/temporadauno/capitulo.html")

def cortitos(request):
    return render(request,"CortosApp/temporadauno/cortitos.html")

def espacio(request):
    return render(request,"CortosApp/temporadauno/espacio.html")

def servilletas(request):
    return render(request,"CortosApp/temporadauno/servilletas.html")

def perdonen(request):
    return render(request,"CortosApp/temporadauno/perdonen.html")

def marmota(request):
    return render(request,"CortosApp/temporadauno/marmota.html")

def muerte(request):
    return render(request,"CortosApp/temporadauno/muerte.html")

def esotericos(request):
    return render(request,"CortosApp/temporadauno/esotericos.html")

def efemerides(request):
    return render(request,"CortosApp/temporadauno/efemiredes.html")

def ninos(request):
    return render(request,"CortosApp/temporadauno/ninos.html")

def publicidad(request):
    return render(request,"CortosApp/temporadauno/publicidad.html")

def mamberto(request):
    return render(request,"CortosApp/temporadauno/mamberto.html")

def charles(request):
    return render(request,"CortosApp/temporadauno/charles.html")

