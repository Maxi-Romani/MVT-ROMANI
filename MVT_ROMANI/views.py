from pipes import Template
from django.http import HttpResponse

from datetime import datetime
from django.shortcuts import render


def saludo(request):
	return HttpResponse("Hola Django - Coder")

def despedida(request):
    return HttpResponse("Chau, fue un gusto")

def fecha_actual(request):
    fecha=datetime.now().date()
    mensaje=f"Hoy es {fecha}"
    return HttpResponse(mensaje)

def prueba(request):
    context={
        "Nombre" : "Maximiliano",
        "Apellido" : "Romani",
        "Fechanacimiento" : "08/12/1985"
    }
    return render(request, "template1.html", context=context)
    


