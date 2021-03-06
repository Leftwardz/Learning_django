from django.shortcuts import render, redirect
from .models import Produto
from .form import ProdutoForm

import time

def home(request):
    data = {}
    data['hoje'] = time.strftime('%d/%m/%Y', time.localtime())
    data['teste'] = [f'Teste {i}' for i in range(10)]
    return render(request, 'cadastrar_app/home.html', data)

def listagem(request):
    data = {}
    data['produtos'] = Produto.objects.all()

    return render(request, 'cadastrar_app/lista.html', data)

def novo_produto(request):
    data = {}
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    return render(request, 'cadastrar_app/novo_produto.html', data)

def update(request, pk):
    data = {}
    produto = Produto.objects.get(pk=pk)
    form = ProdutoForm(request.POST or None, instance=produto)
    data['form'] = form
    data['produto'] = produto
    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    return render(request, 'cadastrar_app/novo_produto.html', data)

def delete(request, pk):
    produto = Produto.objects.get(pk=pk)
    produto.delete()
    return redirect('url_listagem')
