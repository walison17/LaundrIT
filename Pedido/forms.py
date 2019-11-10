from django.forms import ModelForm
from django.contrib.auth.hashers import make_password
from django.db import transaction

from Home.models import Cliente
from  Pedido.models import Item, Pedido, Roupa, Status


class ItemForm(ModelForm):
    
    class Meta:
        model = Item

        fields = ['quantidade', 'servico', 'pedido']


class PedidoForm(ModelForm):

    class Meta:
        model = Pedido

        fields = ['status']

class RoupaForm(ModelForm):

    class Meta:
        model = Roupa

        fields = ['nome_peca', 'preco']


class StatusForm(ModelForm):

    class Meta:
        model = Status

        fields = ['descricao', 'data_postagem', 'status_pedido']
