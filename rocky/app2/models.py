from django.db import models

# Create your models here.

class Intrebare(models.Model):
    text = models.TextField()
    punctaj = models.FloatField()

class VariantaRaspuns(models.Model):
    intrebare = models.ForeignKey(Intrebare, on_delete=models.CASCADE)
    corect = models.BooleanField(default=False)
    feedback = models.CharField(max_length=50, null=True, blank=True)