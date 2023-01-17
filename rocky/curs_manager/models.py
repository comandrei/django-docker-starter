from django.db import models

# Create your models here.
class Student(models.Model):
    nume = models.TextField()
    prenume = models.TextField()
    an = models.IntegerField(default=1, db_index=True)
    telefon = models.TextField(null=True, blank=True)
    cnp = models.IntegerField(unique=True, null=True, blank=True)