from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def salut(request):
    gigel = "Gigel"
   #1/0
    return HttpResponse("salutare")

def studenti(request):
    lista_studenti = ["Student 1", "Student 2", "Student3"]
    studenti_formatat = ", ".join(lista_studenti)
    studenti_formatat = "<br /> ".join(lista_studenti)
    return HttpResponse(studenti_formatat)
