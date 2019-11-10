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
from .models import Pedido, Item, Roupa, Status

from .forms import PedidoForm, ItemForm, StatusForm
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
    roupas = Roupa.objects.all()
    pedido = Pedido.objects.all()
    servico =  Servico.objects.all()
    status = Status.objects.all()

    return render(request, 'pedido/pedidos.html', {
            'cliente': cliente,
            'roupas': roupas,
            'status': status,
            'pedido': pedido,
            'servico': servico,
                })

def adicionar_item(request):
    return render(request, 'pedido/pedidos.html')

def update_item(request):
    return render(request, 'pedido/pedidos.html')

    
