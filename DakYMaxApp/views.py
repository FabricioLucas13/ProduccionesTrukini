from django.shortcuts import render, HttpResponse

# Create your views here.

def dakymax(request):
    return render(request,"DakYMaxApp/dakymax.html")

def temporada1(request):
    return render(request,"DakYMaxApp/temporada1.html")

def llegada(request):
    return render(request,"DakYMaxApp/temporadauno/llegada.html")

def imperfecto(request):
    return render(request,"DakYMaxApp/temporadauno/imperfecto.html")

def trenzado(request):
    return render(request,"DakYMaxApp/temporadauno/trenzado.html")