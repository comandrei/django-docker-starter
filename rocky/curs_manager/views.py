from django.shortcuts import render
from django.http import HttpResponse

from .models import Student
# Create your views here.

def salut(request):
    gigel = "Gigel"
   #1/0
    return HttpResponse("salutare")

def studenti(request):
    if 'an' in request.GET:
        try:
            lista_studenti = Student.objects.filter(an=request.GET['an'])
        except ValueError:
            lista_studenti = []
    else: 
        lista_studenti = Student.objects.all()
    context = {
        "studenti": lista_studenti
    }
    return render(request, "studenti.html", context)



def contact(request):
    return render(request, "contact.html")