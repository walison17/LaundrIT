from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_list_or_404
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Q, Value
from django.contrib.auth.models import User
from Home.models import Cliente
from django.http import HttpResponseNotFound
from Servico.models import Servico
from .models import Pedido, Item, Roupa, Status, Suporte

from .forms import PedidoForm, ItemForm, StatusForm, SuporteForm
from Servico.forms import ServicoForm

# Create your views here.


# --- admin... ---

def pedidos_admin(request):
    cliente = Cliente.objects.all()
    roupas = Roupa.objects.all()
    pedido = Pedido.objects.all()
    servico =  Servico.objects.all()
    status = Status.objects.all()

    return render(request, 'pedido/pedidos_admin.html', {
            'cliente': cliente,
            'roupas': roupas,
            'status': status,
            'pedido': pedido,
            'servico': servico,
                })

def pedidos_usuario(request):
    cliente = Cliente.objects.all()
    itens = Item.objects.all()
    roupas = Roupa.objects.all()
    pedido = Pedido.objects.all()
    servico =  Servico.objects.all()
    status = Status.objects.all()

    return render(request, 'pedido/pedidos.html', {
            'cliente': cliente,
            'roupas': roupas,
            'status': status,
            'itens': itens,
            'pedido': pedido,
            'servico': servico,
                })

def adicionar_item(request):
    return render(request, 'pedido/pedidos.html')

def update_item(request):
    return render(request, 'pedido/pedidos.html')

def pagamento(request):
    return render(request, 'pedido/pagamento.html')

def suporte_admin(request):
    return render(request, 'pedido/suporte_admin.html')

def suporte_usuario(request):
    if request.method != 'POST':
        return render(request, 'pedido/suporte.html')

    email = request.POST.get('email', None)
    mensagem = request.POST.get('mensagem', None)
    numero_pedido  = request.POST.get('numero_pedido', None)

    if not email or not mensagem:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'pedido/suporte.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'E-mail Inválido.')
        return render(request, 'pedido/suporte.html')

    cpf = request.user.cliente.cpf
    nome_cliente = request.user.nome_cliente
    telefone = request.user.telefone

    comentario = Suporte.objects.create(nome_cliente=nome_cliente, email=email, \
        cpf=cpf, telefone=telefone, mensagem=mensagem, numero_pedido=numero_pedido)


    return render(request, 'pedido/suporte.html')


    
