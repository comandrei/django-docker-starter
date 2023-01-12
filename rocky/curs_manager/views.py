from django.shortcuts import render
from django.http import HttpResponse

from .models import Student
# Create your views here.

def salut(request):
    gigel = "Gigel"
   #1/0
    return HttpResponse("salutare")

def studenti(request):
    lista_studenti = ["Student 1", "Student 2", "Student3"]
    lista_studenti = Student.objects.all()
    #studenti_formatat = ", ".join(lista_studenti)
    #studenti_formatat = "<br /> ".join(lista_studenti)
    studenti_formatat = [(student.nume, student.prenume) for student in lista_studenti]
    #studenti_formatat = "<br /> ".join(studenti_formatat)
    output_string = ""
    for student in lista_studenti:
        rand = f"{student.nume} {student.prenume} <br />"
        output_string += rand
    return HttpResponse(output_string)


def contact(request):
    return render(request, "contact.html")