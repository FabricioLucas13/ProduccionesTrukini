from django.shortcuts import render, HttpResponse

# Create your views here.

def edificio(request):
    return render(request,"EdificioApp/edificio.html")

def afortunada(request):
    return render(request,"EdificioApp/temporadauno/afortunada.html")

def dinero(request):
    return render(request,"EdificioApp/temporadauno/dinero.html")

def nueva(request):
    return render(request,"EdificioApp/temporadauno/nueva.html")