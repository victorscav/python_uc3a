from django.db import models

class Tag(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class CategoriaProduto(models.Model):
    descricao = models.CharField(
        max_length=100,
        null=True,
        blank=True
        )

    def __str__(self):
        return self.descricao

class Marca(models.Model):
    nome = models.CharField(
        max_length=100,
        )
    descricao = models.TextField(
        blank=True
        )

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(
        max_length=100,
        )
    
    descricao = models.TextField(
        blank=True
        )
    
    modelo = models.CharField(
        max_length=100,
          blank=True
          )
    
    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2)
    
    imagem = models.ImageField(
        upload_to='produtos/', 
        blank=True, 
        null=True)
    
    qt_estoque = models.PositiveIntegerField(
        blank=True,
        null=True

    )
    
    tamanho = models.CharField(
        max_length=50, blank=True
        )

    categoria_produto = models.ForeignKey(
        CategoriaProduto, 
        on_delete=models.PROTECT
        )
    
    marca = models.ForeignKey(
        Marca, 
        on_delete=models.PROTECT,
        null=True,
        blank=True
        )
    
    tags = models.ManyToManyField(
        Tag, 
        blank=True
        )

    def __str__(self):
        return self.nome