from django.forms import ModelForm
from django.contrib.auth.hashers import make_password
from django.db import transaction

from Home.models import Cliente
from .models import Servico
from Pedido.models import Item
from Pedido.models import Pedido


class ServicoForm(ModelForm):

    class Meta:
        model = Servico

        fields = ['nome_servico', 'preco_servico']


