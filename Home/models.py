from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from datetime import datetime
from datetime import time

# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_cliente = models.CharField(max_length=50, blank=False, verbose_name=u'Nome Cliente')
    rg = models.CharField(max_length=14,
                          blank=True, verbose_name=u'RG')
    cpf = models.BigIntegerField( unique=True, verbose_name=u' CPF- ', validators=[
        MaxValueValidator(99999999999),
        MinValueValidator(11111111111)
    ])
    endereco = models.CharField(max_length=60, verbose_name=u'Endereço')
    telefone = models.BigIntegerField(
        null=True, blank=True, verbose_name=u'Telefone')
    
    def __str__(self):
        return self.user.username