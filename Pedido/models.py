from django.db import models
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from datetime import datetime
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

from model_utils.models import TimeStampedModel, UUIDModel

from Home.models import Cliente 

# Create your models here.

class StatusPedido(models.Model):
    PEDIDO_ATIVO = 'Pedido Ativo'
    PEDIDO_FINALIZADO = 'Pedido Finalizado'
    PEDIDO_CANCELADO = 'Pedido Cancelado'
    STATUS =(
        (PEDIDO_ATIVO, 'Pedido Ativo'),
        (PEDIDO_FINALIZADO, 'Pedido Finalizado'),
        (PEDIDO_CANCELADO, 'Pedido Cancelado')
    )
    situacao_pedido = models.CharField(
        'Situação', max_length=50, choices=STATUS, default=PEDIDO_ATIVO)

    def __str__(self):
        return ' %s ' % self.situacao_pedido

class Pedido(UUIDModel, TimeStampedModel):
    BOLETO = 'Boleto Bancário'
    CARTAO_DEBITO = 'Cartão de Débito'
    CARTAO_CREDITO = 'Cartão de Crédito'
    TRANSFERENCIA = 'Transferência Bancária'
    PAGAMENTO =(
        (BOLETO, 'Boleto Bancário'),
        (CARTAO_DEBITO, 'Cartão de Débito'),
        (CARTAO_CREDITO, 'Cartão de Crédito'),
        (TRANSFERENCIA, 'Transferência Bancária')
    )
    id = models.AutoField(primary_key=True)
    solicitante = models.ForeignKey(Cliente,
        max_length=50,
        verbose_name="Nome Cliente",
        related_name = 'solicitante',
        on_delete = models.CASCADE)
    
    data_solicitacao = models.DateTimeField(
        default=timezone.now, verbose_name="Data da Postagem")

    data_entrega = models.DateTimeField(default=timezone.now, verbose_name="Data de Entrega"
    )

    valor_total = models.DecimalField(
        'Valor Total',
        max_digits=7,
        decimal_places=2,
        null=True,
        editable=False
    )
    pagamento = models.CharField('Pagamento', max_length=50, choices=PAGAMENTO, default=BOLETO, null=False, blank=False)
    situacao_pedido = models.ForeignKey(StatusPedido, verbose_name="Status Pedido", on_delete=models.PROTECT)
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

class Status(models.Model):
    id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(
        Pedido,
        verbose_name = 'Pedido',
        related_name = 'pedido',
        on_delete = models.PROTECT)
    comentario = models.TextField(null=False, blank=False, verbose_name="Comentar Status")
    situacao_pedido = models.ForeignKey(StatusPedido, verbose_name="Status do Pedido", on_delete=models.PROTECT)
    data_comentario = models.DateTimeField(default=timezone.now, verbose_name="Data do Comentario")


    def __str__(self):
        return 'id : %s status: %s '% (self.id, self.situacao_pedido)


class Roupa(UUIDModel, TimeStampedModel):
    id = models.AutoField(primary_key=True)
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
        self.preco_unitario =  self.quantidade * (self.servico.preco_servico + self.roupa.preco_roupa)
        return super().save(*args, **kwargs)




class Suporte(models.Model):
    id = models.AutoField(primary_key=True)
    nome_cliente = models.CharField(max_length=50, verbose_name="Nome do Cliente")
    email = models.CharField(max_length=60, blank=False, null=False, verbose_name="E-mail do Cliente")
    cpf = models.BigIntegerField(unique=False, verbose_name=u' CPF ', validators=[
        MaxValueValidator(99999999999),
        MinValueValidator(11111111111)
    ])
    mensagem = models.TextField(max_length=255, blank=False, null=False,)
    data_mensagem = models.DateTimeField(default=timezone.now(), blank=True, null=True)
    resposta = models.TextField(max_length=255, blank=False, null=False)
    #numero_pedido = models.ForeignKey(Pedido, null=True, blank=True, verbose_name="Número do Pedido", on_delete=models.PROTECT)

    def __str__(self):
        return '%s ' % (self.nome_cliente)




        