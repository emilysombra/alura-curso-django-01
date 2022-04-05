from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def receita(request):
    dados = {'nome_receita': 'gelo cozido'}
    return render(request, 'receita.html', dados)
