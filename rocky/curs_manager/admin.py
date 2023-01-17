from django.contrib import admin

from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ("nume", "prenume", "an")
    list_filter = ("an", )
    search_fields = ("nume", "prenume")

admin.site.register(Student, StudentAdmin)