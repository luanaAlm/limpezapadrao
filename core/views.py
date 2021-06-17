from django.shortcuts import render
from .form import ClienteForm
from .models import Cliente, Depoimento, Parceiro, Sofa, Cama, Tapete, Automovel


def index(request):
    sofas = Sofa.objects.all()
    camas = Cama.objects.all()
    tapetes = Tapete.objects.all()
    automoveis = Automovel.objects.all()
    depoimentos = Depoimento.objects.all()
    parceiros = Parceiro.objects.all()
    return render(request, "index.html", {
        "sofas": sofas,
        "camas": camas,
        "tapetes": tapetes,
        "automoveis": automoveis,
        "depoimentos": depoimentos,
        "parceiros": parceiros
    })
