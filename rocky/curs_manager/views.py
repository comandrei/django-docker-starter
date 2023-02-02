from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.db.models import F

from .forms import ContactForm, CursForm
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
    return render(request, "nume_fisier.html", context)



def contact(request):
    return render(request, "public/contact.html")

def contact_2(request):
    if request.method == "POST":
        formular = ContactForm(request.POST)
        if formular.is_valid():
            return redirect("/cursuri")
    else:
        formular = ContactForm()
    context = {
        "formular": formular,
    }
    return render(request, "contact.html", context)

def cursuri(request):
    cursuri = Curs.objects.all().prefetch_related("student_set")
    context = {
        "cursuri": cursuri
    }
    return render(request, "curs.html", context)


def curs(request, curs_nume, curs_id):
    #curs = Curs.objects.first() # Curs.objects.all()[0]
    #curs = Curs.objects.all()[1]
    curs_obj = get_object_or_404(Curs, id=curs_id)
    context = {
        "my_var": curs_obj,
    }
    return render(request, "curs_detail.html", context)

def promoveaza_an(request, param_an):
    studenti = Student.objects.filter(an=param_an)
    context = {
        "studenti": studenti
    }
    # for student in studenti:
    #     student.an = student.an + 1
    #     student.save()
    #studenti.update(an=param+1)
    #studenti.update(an=1)

    studenti = Student.objects.all()
    studenti.update(an=F('an') + 1)


    return render(request, "promovare.html", context)


def add_curs(request):
    mesaj = None
    if request.method == "POST":
        form = CursForm(data=request.POST)
        if form.is_valid():
            result = form.save()
            return redirect(
                reverse("detaliu-curs", kwargs={"curs_nume": result.nume, "curs_id": result.id}))
    else:
        form = CursForm()
    context = {
        "form": form,
        "mesaj": mesaj
    }
    return render(request, "add_curs.html", context)

def edit_curs(request, curs_nume, curs_id):
    curs_obj = get_object_or_404(Curs, id=curs_id)
    if request.method == "POST":
        form = CursForm(data=request.POST, instance=curs_obj)
        if form.is_valid():
            result = form.save()
            return redirect(
                reverse("detaliu-curs", kwargs={"curs_nume": result.nume, "curs_id": result.id}))
    else:
        form = CursForm(instance=curs_obj)
    context = {
        "form": form
    }
    return render(request, "add_curs.html", context)