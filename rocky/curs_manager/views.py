from django.shortcuts import render
from django.http import HttpResponse

from .models import Student
# Create your views here.

def salut(request):
    gigel = "Gigel"
   #1/0
    return HttpResponse("salutare")

def studenti(request):
    lista_studenti = Student.objects.all()
    context = {
        "studenti": lista_studenti
    }
    return render(request, "studenti.html", context)



def contact(request):
    return render(request, "contact.html")