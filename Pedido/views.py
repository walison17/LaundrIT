from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_list_or_404
from django.contrib.auth.decorators import login_required
from django.core.validators import validte_email
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.contrib.auth.models import User
from Home.models import Cliente
from django.http import HttpResponseNotFound
from Servico.models import Servico
from .models import Pedido, Item

from .forms import PedidoForm, ItemForm
from Servico.forms import ServicoForm

# Create your views here.


# --- admin... ---
def pedidos_admin(request):
    return render(request, 'pedido/pedidos_admin.html')

def pedidos_usuario(request):
    return render(request, 'pedido/pedidos.html')

def adicionar_item(request):
    return render(request, 'pedido/pedidos.html')

def update_item(request):
    return render(request, 'pedido/pedidos.html')
    
