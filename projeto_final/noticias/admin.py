from django.contrib import admin
from .models import Tag, CategoriaNoticia, Noticia, Comentario

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(CategoriaNoticia)
class CategoriaNoticiaAdmin(admin.ModelAdmin):
    pass

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    pass

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    pass