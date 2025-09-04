from django.contrib import admin
from .models import Perfil
from .models import Endereco

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    pass
#    list_display = ('user', 'cpf', 'tel_celular', 'dt_nascimento')
#    search_fields = ('user__username', 'user__email', 'cpf', 'tel_celular')
#    list_filter = ('genero',)

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    pass