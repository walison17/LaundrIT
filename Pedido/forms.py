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

        fields = ['solicitante','status', 'data_solicitacao', 'pagamento', 'data_entrega']

class RoupaForm(ModelForm):

    class Meta:
        model = Roupa

        fields = ['nome_peca', 'preco_roupa']


class StatusForm(ModelForm):

    class Meta:
        model = Status

        fields = ['comentario', 'status_pedido', 'data_comentario']