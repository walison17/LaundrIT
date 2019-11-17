from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
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
from django.utils import timezone

from .forms import PedidoForm, ItemForm, StatusForm, SuporteForm
from Servico.forms import ServicoForm

# Create your views here.


# --- admin... ---

@login_required
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

@login_required
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

@login_required
def adicionar_item(request):
    return render(request, 'pedido/pedidos.html')

@login_required
def update_item(request):
    return render(request, 'pedido/pedidos.html')

@login_required
def pagamento(request):
    return render(request, 'pedido/pagamento.html')

@login_required
def suporte_admin(request):
    suporte = Suporte.objects.all().order_by('-data_mensagem')

    return render(request, 'pedido/suporte_admin.html', {'suporte' : suporte})

@login_required
def suporte_usuario(request):
    if request.method != 'POST':
        return render(request, 'pedido/suporte.html')

    email = request.POST.get('email', None)
    mensagem = request.POST.get('mensagem', None)

    if not email or not mensagem:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'pedido/suporte.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'E-mail Inválido.')
        return render(request, 'pedido/suporte.html')


    nome_cliente = request.user.username 
    cpf = request.user.cliente.cpf

    suporte = Suporte.objects.create(email=email, nome_cliente=nome_cliente, \
        cpf=cpf, mensagem=mensagem)
    suporte.save()

    messages.success(request, 'Mensagem Enviada com sucesso! Aguarde pelo retorno.')
    return redirect('inicial')

    return render(request, 'pedido/suporte.html')



    return render(request, 'pedido/suporte.html')


@login_required
def responder_suporte(request, id):
    if request.user.is_superuser:
        suporte = Suporte.objects.all()
        suporte = get_object_or_404(Suporte, pk=id)
        form = SuporteForm(request.POST or None, request.FILES or None)
        print(form)
        resposta = request.POST.get('resposta', None)
        form.email = suporte.email
        form.nome_cliente = suporte.nome_cliente
        form.cpf = suporte.cpf
        form.mensagem = suporte.mensagem
        form.resposta = resposta
        form.data_mensagem = timezone.now()
        print(form.email)
        print(form.nome_cliente)
        print(form.cpf)
        print(form.mensagem)
        print(form.resposta)

        if not resposta:
            messages.error(request, 'Você precisa enviar uma resposta..')
            return render(request, 'pedido/responder_suporte.html', {'suporte': suporte})
        subject = form.mensagem
        message = form.resposta
        from_email = settings.EMAIL_HOST_USER
        to_list = ['janaina.antunes1@bol.com']
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        print('to aqui')

        if form.is_valid():    
            form.save()
            save_it = form.save()
            save_it.save()
            subject = form.mensagem
            message = form.resposta
            from_email = settings.EMAIL_HOST_USER
            to_list = ['janaina.antunes1@bol.com']
            print('to aqui')

            send_mail(subject, message, from_email, to_list, fail_silently=True)
            return redirect('suporte_admin')

        print('to aqui fora')

        return render(request, 'pedido/responder_suporte.html', {
            'suporte': suporte,
        })
    else:
        return HttpResponseNotFound("Acesso Negado!")

    
