from django.contrib import admin

from .models import Student, Adresa, AdresaNoua, StudentProfile, Curs
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ("nume", "prenume", "an")
    list_filter = ("an", ("cursuri", admin.RelatedOnlyFieldListFilter))
    list_per_page = 3
    # Student.objects.filter(Q(nume__icontains=request.GET["q"]) | Q(prenume__icontains=request.GET["q"]))
    search_fields = ("nume", "prenume")

admin.site.register(Student, StudentAdmin)

admin.site.register(Adresa)

class AdresaAdmin(admin.ModelAdmin):
    list_display = ("strada", "judet", "student")
    list_filter = ("student", )

admin.site.register(AdresaNoua, AdresaAdmin)
admin.site.register(StudentProfile)
admin.site.register(Curs)