from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class CategoriaNoticia(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Noticia(models.Model):
    STATUS_CHOICES = [
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
        ('inativo', 'Inativo'),
    ]

    titulo = models.CharField(max_length=200)
    resumo = models.TextField(blank=True)
    conteudo = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='rascunho')

    categoria_noticia = models.ForeignKey(CategoriaNoticia, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comentarios')
    conteudo = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return f'Comentário de {self.user.username} em "{self.noticia.titulo}"'
