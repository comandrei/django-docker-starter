from django.db import models

# Create your models here.
class Student(models.Model):
    nume = models.TextField()
    prenume = models.TextField()
    an = models.IntegerField()
    telefon = models.TextField()