from django.contrib import admin
# Register your models here.

from .models import Intrebare, VariantaRaspuns

class VariantaRaspunsAdmin(admin.ModelAdmin):
    list_display = ("intrebare", "text", "corect")
    list_filter = ("intrebare", "corect")

admin.site.register(Intrebare)
admin.site.register(VariantaRaspuns, VariantaRaspunsAdmin)