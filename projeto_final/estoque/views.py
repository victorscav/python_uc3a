from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib import messages


# Models
from .models import Produto, Tag, CategoriaProduto

# Forms


def index(request):

    context = {
        'titulo' : 'Bem vindo à Página de Produtos!'
    }

    return render(request, 'estoque/index_estoque.html', context)