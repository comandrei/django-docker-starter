from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def validate_no_a(value):
    if "a" in value:
        raise ValidationError("Caracter nepermis")

class StudentManager(models.Manager):

    def boboci(self):
        return self.filter(an=1)

# Create your models here.
class Student(models.Model):

    class Meta:
        ordering = ("an", "nume", "prenume")
        unique_together = ("nume", "prenume", "an")

    nume = models.TextField()
    prenume = models.TextField()
    an = models.IntegerField(default=1, db_index=True)
    telefon = models.TextField(null=True, blank=True)
    cnp = models.CharField(unique=True, null=True, blank=True, max_length=13,
                                validators=[MinLengthValidator(13), validate_no_a])
    cursuri = models.ManyToManyField("Curs")
    objects = StudentManager()

    def __str__(self):
        return f"{self.nume} {self.prenume} | an {self.an}"

class Adresa(Student):
    class Meta:
        verbose_name_plural = "adrese"
    strada = models.CharField(max_length=20)
    judet = models.CharField(max_length=15)
    cod_postal = models.IntegerField()


class AdresaNoua(models.Model):
    class Meta:
        verbose_name_plural = "Adrese Noi"
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    strada = models.CharField(max_length=20)
    judet = models.CharField(max_length=15)
    cod_postal = models.IntegerField()

    def __str__(self):
        return f"{self.strada} {self.judet}"


class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    virsta = models.IntegerField()


class Curs(models.Model):
    class Meta:
        verbose_name_plural = "cursuri"

    nume = models.CharField(max_length=20)
    an = models.IntegerField()
    profesor = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nume} {self.an} | Studenti {self.student_set.count()}"


class Animal(models.Model):
    class Meta:
        abstract = True

    nume = models.CharField(max_length=10)

class Pisica(Animal):
    culoare = models.CharField(max_length=10)
    vieti = models.IntegerField(default=9)

class Caine(Animal):
    culoare = models.CharField(max_length=10)
    rasa = models.CharField(max_length=10)
