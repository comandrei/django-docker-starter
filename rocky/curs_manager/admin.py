from django.contrib import admin

from .models import Student, Adresa, AdresaNoua
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ("nume", "prenume", "an")
    list_filter = ("an", )
    # Student.objects.filter(Q(nume__icontains=request.GET["q"]) | Q(prenume__icontains=request.GET["q"]))
    search_fields = ("nume", "prenume")

admin.site.register(Student, StudentAdmin)

admin.site.register(Adresa)

class AdresaAdmin(admin.ModelAdmin):
    list_display = ("strada", "judet", "student")
    list_filter = ("student", )

admin.site.register(AdresaNoua, AdresaAdmin)