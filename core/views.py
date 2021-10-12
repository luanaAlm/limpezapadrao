from django.contrib import messages
from .models import Depoimento, Parceiro, Sofa, Cama, Tapete, Automovel
from .form import ClienteForm
from django.shortcuts import redirect, render


def index(request):
    sofas = Sofa.objects.all()
    camas = Cama.objects.all()
    tapetes = Tapete.objects.all()
    automoveis = Automovel.objects.all()
    depoimentos = Depoimento.objects.all()
    parceiros = Parceiro.objects.all()
    form = ClienteForm()
    return render(request, "index.html", {
        "sofas": sofas,
        "camas": camas,
        "tapetes": tapetes,
        "automoveis": automoveis,
        "depoimentos": depoimentos,
        "parceiros": parceiros,
        "form": form
    })


def cliente_novo(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Sua mensagem foi enviada com sucesso!')
        return redirect('index')
    else:
        messages.error(
            request, 'Houve um erro, reenvie novamente a mensagem!')
        return redirect('index')
