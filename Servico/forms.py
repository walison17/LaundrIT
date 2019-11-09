from django.forms import ModelForm
from django.contrib.auth.hashers import make_password
from django.db import transaction

from Home.models import Cliente
from .models import Servico
from Pedido.models import Item
from Pedido.models import Pedido


class ClienteForm(modelForm):
    
    class Meta:
        model = Cliente

        fields = ['user', 'nome_cliente', 'rg', 'cpf', 'endereco', 'telefone' ]


class ServicoForm(ModelForm):

    class Meta:
        model = Servico

        fields = ['descricao', 'preco']

class ItemForm(ModelForm):
    
    class Meta:
        model = Item

        fields = ['quantidade', 'perco_unitario', 'servico', 'pedido']


class PedidoForm(ModelForm):

    class Meta:
        model = Pedido

        fields = ['valor_total', 'status']


