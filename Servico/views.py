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
from .models import Servico
from Pedido.models import Pedido, Item

from Pedido.forms import PedidoForm, ItemForm
from .forms import ServicoForm


# Create your views here.



def inicial(request):
    return render(request, 'servico/inicial.html')

def pedido_comentar_status(request, id):
    return render(request, 'servico/status_comentar_admin.html')

def administrador_status(request):
    return render(request, 'servico/status_admin.html')

def administrador_usuario(request):
    return render(request, 'servico/inicial.html')

def administrador_item(request):
    return render(request, 'servico/inicial.html')

def administrador_servico(request):
    return render(request, 'servico/inicial.html')









def historico(request):
    return render(request, 'servico/historico.html')

def status(request):
    return render(request, 'servico/status.html')

def buscar_por_status(request):
    return render(request, 'servico/buscar_por_status.html')

def suporte(request):
    return render(request, 'servico/suporte,html')