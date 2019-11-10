from django.forms import ModelForm
from django.contrib.auth.hashers import make_password
from django.db import transaction

from Home.models import Cliente
from  Pedido.models import Item, Pedido


class ItemForm(ModelForm):
    
    class Meta:
        model = Item

        fields = ['quantidade', 'servico', 'pedido']


class PedidoForm(ModelForm):

    class Meta:
        model = Pedido

        fields = ['status']
