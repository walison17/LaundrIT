from django.db import models

from model_utils.models import TimeStampedModel, UUIDModel


class Servico(UUIDModel, TimeStampedModel):
    id = models.AutoField(primary_key=True)
    nome_servico = models.CharField('Nome Serviço', max_length=100)
    preco_servico = models.DecimalField('Preço', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'serviço'
        verbose_name_plural = 'serviços'
        ordering = ('-nome_servico',)

    def __str__(self):
        return self.nome_servico
