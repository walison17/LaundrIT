from django.db import models
from django.db.models import Sum, F, ExpressionWrapper, DecimalField

from model_utils.models import TimeStampedModel, UUIDModel

# Create your models here.

class Pedido(UUIDModel, TimeStampedModel):
    PEDIDO_REALIZADO = 0
    CONCLUIDO = 1
    CANCELADO = 2
    STATUS =(
        (PEDIDO_REALIZADO, 'Pedido Realizado'),
        (CONCLUIDO, 'Concluído'),
        (CANCELADO, 'Cancelado')
    )

    valor_total = models.DecimalField(
        'Valor Total',
        max_digits=7,
        decimal_places=2,
        null=True,
        editable=False
    )
    status = models.PositiveSmallIntegerField(
        'Situação', choices=STATUS, default=PEDIDO_REALIZADO
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

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'itens'
        ordering = ('-created',)

    def __str__(self):
        return f'{self.quantidade} x {self.servico}'

    def save(self, *args, **kwargs):
        self.preco_unitario = self.servico.preco
        return super().save(*args, **kwargs)

        