from django.contrib import admin
# Register your models here.

from .models import Intrebare, VariantaRaspuns

class VariantaRaspunsAdmin(admin.ModelAdmin):
    list_display = ("intrebare", "text", "corect")
    list_filter = ("intrebare", "corect")

class RaspunsInline(admin.StackedInline):
    model = VariantaRaspuns
    extra = 0
    fieldsets = (
        ("", {"fields": ["text", "corect", "feedback"]}),
    )

class IntrebareAdmin(admin.ModelAdmin):
    inlines = (RaspunsInline, )

admin.site.register(Intrebare, IntrebareAdmin)
admin.site.register(VariantaRaspuns, VariantaRaspunsAdmin)