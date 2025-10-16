from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Produto, Protuto_Tag, Categoria

def teste(request):
    context = {
        'titulo': 'Bem-vindo à Página de Produtos!'
    }
    return render(request, 'estoque/index_static.html', context)

def index(request):
    context = {
        'titulo': 'Bem-vindo à Página de Produtos!'
    }
    return render(request, 'estoque/index_estoque.html', context)

class ProdutoListView(ListView):
    model = Produto
    template_name = 'estoque/produto_list.html'
    context_object_name = 'produtos'
    ordering = ['nome']
    paginate_by = 10

class ProdutoTabelaListView(ListView):
    model = Produto
    template_name = 'estoque/produto_tabela_list.html'
    context_object_name = 'produtos'
    ordering = ['nome']
    paginate_by = 10

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'estoque/produto_detail.html'
    context_object_name = 'produto'

class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'estoque/produto_form.html'
    fields = ['nome', 'descricao', 'preco', 'estoque', 'disponivel', 'imagem', 'categoria', 'tag']
    success_url = reverse_lazy('estoque:produto_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Cadastrar Novo Produto'
        return context

class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'estoque/produto_form.html'
    fields = ['nome', 'descricao', 'preco', 'estoque', 'disponivel', 'imagem', 'categoria', 'tag']
    success_url = reverse_lazy('estoque:produto_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Editar Produto'
        return context

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'estoque/produto_confirm_delete.html'
    success_url = reverse_lazy('estoque:produto_list')
    context_object_name = 'produto'

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'estoque/categoria_list.html'
    context_object_name = 'categorias'
    ordering = ['identificacao']
    paginate_by = 10

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'estoque/categoria_detail.html'
    context_object_name = 'categoria'

class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'estoque/categoria_form.html'
    fields = ['identificacao', 'descricao']
    success_url = reverse_lazy('estoque:categoria_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Cadastrar Nova Categoria'
        return context

class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'estoque/categoria_form.html'
    fields = ['identificacao', 'descricao']
    success_url = reverse_lazy('estoque:categoria_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Editar Categoria'
        return context

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'estoque/categoria_confirm_delete.html'
    success_url = reverse_lazy('estoque:categoria_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Excluir Categoria'
        return context

# Views corrigidas para Protuto_Tag
class ProtutoTagListView(ListView):
    model = Protuto_Tag
    template_name = 'estoque/protuto_tag_list.html'
    context_object_name = 'tags'

class ProtutoTagCreateView(CreateView):
    model = Protuto_Tag
    fields = ['identificacao', 'descricao']
    template_name = 'estoque/protuto_tag_form.html'
    success_url = reverse_lazy('estoque:protuto_tag_list')

class ProtutoTagUpdateView(UpdateView):
    model = Protuto_Tag
    fields = ['identificacao', 'descricao']
    template_name = 'estoque/protuto_tag_form.html'
    success_url = reverse_lazy('estoque:protuto_tag_list')

class ProtutoTagDeleteView(DeleteView):
    model = Protuto_Tag
    template_name = 'estoque/protuto_tag_confirm_delete.html'
    success_url = reverse_lazy('estoque:protuto_tag_list')

class ProtutoTagDetailView(DetailView):
    model = Protuto_Tag
    template_name = 'estoque/protuto_tag_detail.html'
    context_object_name = 'tag'
