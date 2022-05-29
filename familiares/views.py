from tkinter.font import families
from unicodedata import name
from django.shortcuts import render

# Create your views here.
def familiares(request):
    context={  }
    return render(request, "familiares.html", context=context)
    