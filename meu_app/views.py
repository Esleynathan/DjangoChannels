from django.shortcuts import render, redirect
from . models import Sala
from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse

def entrar(request):
    if request.method == "GET":
        return render(request, 'entrar.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        sala = Sala.objects.filter(Q(nome = nome) & Q(senha = senha)).first()

        if sala:
            return redirect(reverse('chat', args=(sala.nome, )))
        else:
            return HttpResponse('Nome ou senha inexistentes.')
        
def chat(request, nome):
    
    return render(request, 'chat.html', {'nome': nome})