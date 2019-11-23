from django.forms import ModelForm
from django import forms
from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.forms import formset_factory

from Home.models import Cliente
from  Pedido.models import Item, Pedido, Roupa, Status, Suporte


class ItemForm(forms.Form):
    
    class Meta:
        model = Item

        fields = ['quantidade', 'servico', 'pedido']

ItemFormset = formset_factory(ItemForm)



class PedidoForm(ModelForm):

    class Meta:
        model = Pedido

        fields = ['solicitante', 'data_solicitacao', 'pagamento', 'data_entrega',]

class RoupaForm(ModelForm):

    class Meta:
        model = Roupa

        fields = ['nome_peca', 'preco_roupa']


class StatusForm(ModelForm):

    class Meta:
        model = Status

        fields = ['comentario', 'pedido', 'situacao_pedido', 'data_comentario']


class SuporteForm(ModelForm):
    
    class Meta:
        model = Suporte

        fields = ['nome_cliente', 'email', 'cpf', 'mensagem', 'resposta']
