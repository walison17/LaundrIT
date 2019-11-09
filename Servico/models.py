from django.db import models

from model_utils.models import TimeStampedModel, UUIDModel


class Servico(UUIDModel, TimeStampedModel):
    descricao = models.CharField('Descrição', max_length=100)
    preco = models.DecimalField('Preço', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'serviço'
        verbose_name_plural = 'serviços'
        ordering = ('-descricao',)

    def __str__(self):
        return self.descricao