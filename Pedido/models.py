from django.db import models
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from datetime import datetime
from django.utils import timezone

from model_utils.models import TimeStampedModel, UUIDModel

# Create your models here.

class Status(models.Model):
    id = models.AutoField(primary_key=True)
    PEDIDO_REALIZADO = 0
    CONCLUIDO = 1
    CANCELADO = 2
    STATUS =(
        (PEDIDO_REALIZADO, 'Pedido Realizado'),
        (CONCLUIDO, 'Concluído'),
        (CANCELADO, 'Cancelado')
    )
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    data_postagem = models.DateTimeField(
        default=timezone.now, verbose_name="Data da Postagem")
    status_pedido = models.PositiveSmallIntegerField(
        'Situação', choices=STATUS, default=PEDIDO_REALIZADO
    )

class Pedido(UUIDModel, TimeStampedModel):
    valor_total = models.DecimalField(
        'Valor Total',
        max_digits=7,
        decimal_places=2,
        null=True,
        editable=False
    )
    status = models.ForeignKey(
        Status,
        verbose_name = 'Status',
        related_name = 'status',
        on_delete = models.CASCADE
    )

    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ('-created',)

    def __str__(self):
        return str(self.id)

    def calcular_valor(self):
        expression = ExpressionWrapper(
            F('quantidade') * F('preco_unitario'), output_field=DecimalField()
        )
        return self.items.aggregate(valor_total=Sum(expression))['valor_total']

class Roupa(UUIDModel, TimeStampedModel):
    nome_peca = models.CharField('Nome da Peça',  max_length=50)
    preco_roupa = models.DecimalField('Preço', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Roupa'
        verbose_name_plural = 'Roupas'
        ordering = ('-nome_peca',)

    def __str__(self):
        return self.nome_peca

class Item(TimeStampedModel):
    quantidade = models.PositiveIntegerField('Quantidade', default=1)
    preco_unitario = DecimalField(
        'Preço Unitário', max_digits=5, decimal_places=2, editable=False
    )
    servico = models.ForeignKey(
        'Servico.servico',
        verbose_name='Servico',
        related_name='order_items',
        on_delete=models.PROTECT
    )
    pedido = models.ForeignKey(
        Pedido,
        verbose_name = 'Pedido',
        related_name = 'items',
        on_delete = models.CASCADE
    )
    roupa = models.ForeignKey(
        Roupa,
        verbose_name = 'Roupa',
        related_name = 'roupa_items',
        on_delete = models.CASCADE
    )

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'
        ordering = ('-created',)

    def __str__(self):
        return f'{self.quantidade} x {self.servico} + {self.roupa}'

    def save(self, *args, **kwargs):
        self.preco_unitario =  self.quantidade * (self.servico.preco + self.roupa.preco)
        return super().save(*args, **kwargs)

