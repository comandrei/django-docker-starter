from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def validate_no_a(value):
    if "a" in value:
        raise ValidationError("Caracter nepermis")

# Create your models here.
class Student(models.Model):
    nume = models.TextField()
    prenume = models.TextField()
    an = models.IntegerField(default=1, db_index=True)
    telefon = models.TextField(null=True, blank=True)
    cnp = models.CharField(unique=True, null=True, blank=True, max_length=13,
                                validators=[MinLengthValidator(13), validate_no_a])
            