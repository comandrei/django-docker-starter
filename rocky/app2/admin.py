from django.contrib import admin
# Register your models here.

from .models import Intrebare, VariantaRaspuns

admin.site.register(Intrebare)
admin.site.register(VariantaRaspuns)