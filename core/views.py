from django.shortcuts import render
from django.http import HttpResponse
from .form import ClienteForm
from .models import Cliente, Sofa


def index(request):
    sofas = Sofa.objects.all()
    return render(request, "index.html", {
        "sofas": sofas
    })
