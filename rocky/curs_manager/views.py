from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def salut(request):
    gigel = "Gigel"
   #1/0
    return HttpResponse("salutare")
