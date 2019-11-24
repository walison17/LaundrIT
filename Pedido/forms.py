from django import forms

from .models import Item, Pedido, Roupa, Status, Suporte


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['solicitante', 'pagamento', 'data_entrega']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['servico', 'roupa', 'quantidade', 'pedido']


ItemFormset = forms.inlineformset_factory(Pedido, Item, ItemForm)


class RoupaForm(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = ['nome_peca', 'preco_roupa']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['comentario', 'pedido', 'situacao_pedido', 'data_comentario']


class SuporteForm(forms.ModelForm):
    class Meta:
        model = Suporte
        fields = ['nome_cliente', 'email', 'cpf', 'mensagem', 'resposta']
