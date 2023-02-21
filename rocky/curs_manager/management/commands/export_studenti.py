import csv
from django.core.management.base import BaseCommand

from curs_manager.models import Student

def exporta_studenti(student_qs):
    with open("students.csv", "w") as f:
        fieldnames = ["nume", "prenume", "an", "cnp"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for student in student_qs:
            #print(type(student), student.nume, student.prenume)
            student_row = {
                "nume": student.nume,
                "prenume": student.prenume,
                "an": student.an,
                "cnp": student.cnp 
            }
            writer.writerow(student_row)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        studenti = Student.objects.all()
        exporta_studenti(studenti)