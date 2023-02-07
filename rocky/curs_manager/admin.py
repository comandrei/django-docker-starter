from django.contrib import admin
from django.db.models import F
from .models import Student, Adresa, AdresaNoua, StudentProfile, Curs
# Register your models here.

@admin.action(description="Promovare custom")
def promovare_studenti(modeladmin, request, queryset):
    queryset.update(an=F('an') + 1)
    # Varianta cu mai multe query-uri
    # for student in queryset:
    #     student.an = student.an + 1
    #     student.save()
        #print(student)


class StudentAdmin(admin.ModelAdmin):
    list_display = ("nume", "prenume", "an")
    list_filter = ("an", ("cursuri", admin.RelatedOnlyFieldListFilter), "adresa")
    list_per_page = 3
    # Student.objects.filter(Q(nume__icontains=request.GET["q"]) | Q(prenume__icontains=request.GET["q"]))
    search_fields = ("nume", "prenume")
    actions = (promovare_studenti, )
    change_list_template = "admin/change_list_student.html"

admin.site.register(Student, StudentAdmin)

admin.site.register(Adresa)

class AdresaAdmin(admin.ModelAdmin):
    list_display = ("strada", "judet", "student")
    list_filter = ("student", )

admin.site.register(AdresaNoua, AdresaAdmin)
admin.site.register(StudentProfile)
admin.site.register(Curs)