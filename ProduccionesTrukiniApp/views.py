from django.shortcuts import render, HttpResponse


# Create your views here.

#Inicio de la pagina

def inicio(request):
    return render(request,"ProduccionesTrukiniApp/inicio.html")

