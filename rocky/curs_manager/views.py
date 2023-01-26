from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Student, Curs
# Create your views here.

def salut(request):
    gigel = "Gigel"
   #1/0
    return HttpResponse("salutare")

def studenti(request):
    lista_studenti = Student.objects.all()

    if 'an' in request.GET:
        try:
            lista_studenti = lista_studenti.filter(an__lte=request.GET['an'])
        except ValueError:
            lista_studenti = []
    if 'nume' in request.GET:
        lista_studenti = lista_studenti.filter(nume__icontains=request.GET['nume'])

        
    context = {
        "studenti": lista_studenti,
        "boboci": Student.objects.boboci()
    }
    return render(request, "studenti.html", context)



def contact(request):
    return render(request, "contact.html")


def cursuri(request):
    cursuri = Curs.objects.all().prefetch_related("student_set")
    context = {
        "cursuri": cursuri
    }
    return render(request, "curs.html", context)


def curs(request, curs_nume, curs_id):
    #curs = Curs.objects.first() # Curs.objects.all()[0]
    #curs = Curs.objects.all()[1]
    curs = get_object_or_404(Curs, id=curs_id)
    studenti_inscrisi = curs.student_set.all()
    context = {
        "curs": curs,
        "studenti": studenti_inscrisi
    }
    return render(request, "curs_detail.html", context)