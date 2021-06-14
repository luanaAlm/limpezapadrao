from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import ClienteForm
from .models import Image


def index(request):
    pics = Image.objects.all()
    return render(request, 'index.html')
