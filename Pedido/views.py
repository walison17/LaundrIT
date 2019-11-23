from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_list_or_404
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.utils import timezone
from django.forms import modelformset_factory
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Q, Value
from django.contrib.auth.models import User
from Home.models import Cliente
from Servico.models import Servico
from .models import Pedido, Item, Roupa, Status, Suporte

from .forms import PedidoForm, ItemForm, StatusForm, SuporteForm
from Servico.forms import ServicoForm

# Create your views here.


# --- admin... ---

@login_required
def pedidos_admin(request):
    cliente = Cliente.objects.all()
    roupas = Roupa.objects.all()
    pedido = Pedido.objects.all().filter(situacao_pedido__exact=1)
    paginator = Paginator(pedido, 10)
    page = request.GET.get('p')
    pedido = paginator.get_page(page)
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
def pedidos_usuario(request, ):
    cliente = Cliente.objects.all()
    itens = Item.objects.all()
    roupas = Roupa.objects.all()
    pedido = Pedido.objects.all()
    servico =  Servico.objects.all()
    status = Status.objects.all()
    user = request.user.id
    
    form = PedidoForm(request.POST or None, request.FILES or None)

    form_item = ItemForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

        return redirect('pagamento')


    return render(request, 'pedido/pedidos.html', {
            'cliente': cliente,
            'roupas': roupas,
            'status': status,
            'itens': itens,
            'pedido': pedido,
            'servico': servico,
            'form': form,
            'form_item': form_item
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
    suporte = Suporte.objects.all().order_by('-id')

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
        form = SuporteForm(request.POST or None, request.FILES or None, instance=suporte)
  

        resposta = request.POST.get('resposta', None)
        cpf = suporte.cpf
        email = suporte.email
        nome_cliente = suporte.nome_cliente
        mensagem = suporte.mensagem

      

        if form.is_valid():    
            form.save()
            save_it = form.save()
            save_it.save()
            subject = mensagem
            message = resposta
            from_email = settings.EMAIL_HOST_USER
            to_list = [email, settings.EMAIL_HOST_USER]

            send_mail(subject, message, from_email, to_list, fail_silently=True)
            messages.success(request, f' E-mail enviado com sucesso para {email}')
            return redirect('suporte_admin')
        if not mensagem:
            message.error(request, f'Campo de Mensagem Vázio.' )
            return redirect('responder_suporte')


        return render(request, 'pedido/responder_suporte.html', {
            'suporte': suporte,
        })
    else:
        return HttpResponseNotFound("Acesso Negado!")


def ver_pedido(request, id):
        pedido = get_object_or_404(Pedido, pk=id)
        form = PedidoForm(request.POST or None, request.FILES or None)
        return render(request, 'pedido/ver_pedido.html', {
            'form': form,
            'pedido': pedido,
            } )
    
