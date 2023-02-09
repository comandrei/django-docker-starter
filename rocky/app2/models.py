from django.db import models

# Create your models here.

class Intrebare(models.Model):
    class Meta:
        verbose_name_plural = "Intrebari"

    text = models.TextField()
    punctaj = models.FloatField()

class VariantaRaspuns(models.Model):
    class Meta:
        verbose_name_plural = "Variante Raspuns"
    intrebare = models.ForeignKey(Intrebare, on_delete=models.CASCADE)
    corect = models.BooleanField(default=False)
    feedback = models.CharField(max_length=50, null=True, blank=True)