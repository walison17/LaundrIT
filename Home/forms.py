from django.forms import forms, ModelForm
from .models import Cliente
from .models import User


class ClienteForm(ModelForm):

    class Meta:

        model = Cliente
        fields = ('user', 'rg', 'cpf', 'endereco', 'telefone')