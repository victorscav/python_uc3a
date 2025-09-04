from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
        ('N', 'Prefiro não informar'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')

    foto = models.ImageField(
        upload_to='usuarios/fotos/', 
        blank=True, 
        null=True, 
        help_text='Foto do usuário'
    )

    
    cpf = models.CharField(
        max_length=14, 
        unique=True, 
        default="000.000.000-00",
        help_text='CPF no formato 000.000.000-00'
    )

    tel_fixo = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        help_text='Telefone fixo com DDD'
    )

    tel_celular = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        help_text='Telefone celular com DDD'
    )

    genero = models.CharField(
        max_length=1, 
        choices=GENERO_CHOICES, 
        blank=True, 
        null=True
    )

    desafio_pergunta = models.CharField(
        max_length=255, 
        help_text='Pergunta de recuperação de senha',
        blank=True, 
        null=True
    )

    desafio_resposta = models.CharField(
        max_length=255, 
        help_text='Resposta da pergunta de segurança',
        blank=True, 
        null=True
    )

    dt_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
        null=True, 
        blank=True,
    )

class Endereco(models.Model):
    
    user = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                                related_name='endereco')
    
    cep = models.CharField(
         max_length=9
         )
    
    bairro = models.CharField(
         max_length=100
         )
    
    cidade = models.CharField(
        max_length=100
        )
    
    estado = models.CharField(
         max_length=2
         )
    
    logradouro = models.CharField(
         max_length=255
         )
    
    numero = models.CharField(
         max_length=10
         )
    
    complemento = models.CharField(
         max_length=255,
           blank=True
           )


    def __str__(self):
        return f"Perfil de {self.user.get_full_name() or self.user.username}"

class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

