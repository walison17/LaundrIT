from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.contrib.auth.models import User
from Home.models import Cliente
from django.http import HttpResponseNotFound
from .models import Servico
from Pedido.models import Pedido, Item, Roupa, Status, StatusPedido

from Pedido.forms import PedidoForm, ItemForm, RoupaForm, StatusForm
from .forms import ServicoForm


# Create your views here.


@login_required
def inicial(request):
    cliente = Cliente.objects.all()
    roupas = Roupa.objects.all().order_by('-id')
    servico = Servico.objects.all().order_by('-id')
    paginator_roupa = Paginator(roupas, 3)
    paginator_servico = Paginator(servico, 3)
    roupas = paginator_roupa.get_page('p')
    servico = paginator_servico.get_page('q')
    return render(request, 'servico/inicial.html', {
        'roupas': roupas,
        'servico': servico,
    })


@login_required
def administrador_usuario(request):
    if request.method != 'POST':
        return render(request, 'servico/inicial.html')
    if request.user.is_superuser:
        nome = request.POST.get('nome', None)
        email = request.POST.get('email', None)
        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)
        senha2 = request.POST.get('senha2', None)

        roupas = Roupa.objects.all().order_by('-id')
        servico = Servico.objects.all().order_by('-id')
        paginator_roupa = Paginator(roupas, 3)
        paginator_servico = Paginator(servico, 3)
        roupas = paginator_roupa.get_page('p')
        servico = paginator_roupa.get_page('q')
        
        if not nome or not email or not usuario or not senha or not senha2:
            messages.error(request, 'Nenhum campo pode estar vazio.')
            return render(request, 'servico/inicial.html', {
                'roupas': roupas,
                'servico': servico,
            })
        
        try:
            validate_email(email)
        except:
            messages.error(request, 'E-mail Inválido')
            return render(request, 'servico/inicial.html', {
                'roupas': roupas,
                'servico': servico,
            })
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado.')
            return render(request, 'servico/inicial.html', {
                'roupas': roupas,
                'servico': servico,
            })

        if len(senha) < 6:
            messages.error(
                request, 'Erro! a senha não pode ser menor que 6 caracteres')
            return render(request, 'servico/inicial.html', {
                'roupas': roupas,
                'servico': servico,
            })

        if len(usuario) < 6:
            messages.error(request, 'Usuário precisa ter 6 caracteres ou mais.')
            return render(request, 'servico/inicial.html', {
                'roupas': roupas,
                'servico': servico,
            })
        
        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'Usuário já existe.')
            return render(request, 'servico/inicial.html', {
                'roupas': roupas,
                'servico': servico,
            })

        if senha != senha2:
            messages.error(request, 'Senhas não conferem.')
            return render(request, 'servico/inicial.html', {
                'roupas': roupas,
                'servico': servico,
            })
        
        user = User.objects.create_user(username=usuario, email=email,
        first_name=nome, password=senha, is_superuser = True)
        user.save()

        messages.success(
            request, f' Registrado com sucesso! agora {user.username} é um administrador ')
        return render(request, 'servico/inicial.html', {
            'roupas': roupas,
            'servico': servico,
        })

        return render(request, 'servico/inicial.html', {
            'roupas': roupas,
            'servico': servico,
        })
    else:
        return HttpResponseNotFound("Acesso Negado!")


@login_required
def administrador_roupa(request):
    if request.method != 'POST':
        return render(request, 'servico/inicial.html')
    if request.user.is_superuser:

        form_roupa = RoupaForm(request.POST or None, request.FILES or None)

        nome_item = request.POST.get('nome_item', None)

        if form_roupa.is_valid():
            form_roupa.save()
            messages.success(
                request, f'Item cadastrado com sucesso!')
            return redirect('inicial')
        
        if not form_roupa.is_valid():
            messages.error(
                request, f' Campos não podem estar vazios.')
            return redirect('inicial')
    else:
        return HttpResponseNotFound("Acesso Negado!")


@login_required
def administrador_servico(request):
    if request.method != 'POST':
        return render(request, 'servico/inicial.html')
    if request.user.is_superuser:
        form_servico = ServicoForm(request.POST or None, request.FILES or None)

        nome_servico = request.POST.get('servico', None)

        if form_servico.is_valid():
            form_servico.save()
            messages.success(
                request, f'Serviço cadastrado com sucesso!')
            return redirect('inicial')
        
        if not form_servico.is_valid():
            messages.error(
                request, f' Campos não podem estar vazios.')
            return redirect('inicial')
    else:
        return HttpResponseNotFound("Acesso Negado!")


@login_required
def historico_admin(request):
    if request.user.is_superuser:
        pedido = Pedido.objects.all()
        status = Status.objects.all()

        return render(request, 'servico/historico_admin.html', {
            'pedido': pedido,
            'status': status,
    })
    else:
        return HttpResponseNotFound("Acesso Negado!")


@login_required
def historico_admin_pedido_ativo(request):
    if request.user.is_superuser:
        pedido = Pedido.objects.filter(situacao_pedido=1)
        return render(request, 'servico/historico_admin.html', {
            'pedido': pedido,
        })
    else:
        return HttpResponseNotFound("Acesso Negado!")

@login_required
def historico_admin_pedido_finalizado(request):
    if request.user.is_superuser:
        pedido = Pedido.objects.filter(situacao_pedido=2)
        return render(request, 'servico/historico_admin.html',{
            'pedido': pedido,
        })
    else:
        return HttpResponseNotFound("Acesso Negado!")

@login_required
def historico_admin_pedido_cancelado(request):
    if request.user.is_superuser:
        pedido = Pedido.objects.filter(situacao_pedido=3)
        return render(request, 'servico/historico_admin.html',{
            'pedido': pedido,
        })
    else:
        return HttpResponseNotFound("Acesso Negado!")

@login_required
def status_admin(request):
    if request.user.is_superuser:
        cliente = Cliente.objects.all()
        roupas = Roupa.objects.all()
        servico = Servico.objects.all()
        pedido = Pedido.objects.all()
        status = Status.objects.all().order_by('pedido')
        return render(request, 'servico/status_admin.html', {
            'cliente': cliente,
            'roupas': roupas,
            'servico': servico,
            'pedido': pedido,
            'status': status,
        })
    else:
        return HttpResponseNotFound("Acesso Negado!")

@login_required
def status_comentar_status_pedido(request, id):
    if request.user.is_superuser:
        pedido = get_object_or_404(Pedido, pk=id)
        status = Status.objects.all()
        statuspedido = StatusPedido.objects.all()
        print(statuspedido)
        pedido_escolha = Pedido.objects.all()
        form = StatusForm(request.POST or None, request.FILES or None)
        
        if form.is_valid():
            form.save()
            return redirect('status_admin')
        return render(request, 'servico/status_comentar_admin.html', {
            'form': form,
            'status': status,
            'pedido': pedido,
            'pedido_escolha': pedido_escolha,
            'statuspedido': statuspedido,
        })
    else:
        return HttpResponseNotFound("Acesso Negado!")


# aqui é usuário ... 

@login_required
def historico_usuario(request):
    if request.user.is_superuser:
        return HttpResponseNotFound("Acesso Negado!")
    user = request.user.id
    pedido = Pedido.objects.all().filter(solicitante=user)
    status = Status.objects.all()
    return render(request, 'servico/historico.html', {
        'pedido': pedido,
        'status': status,
    })

@login_required
def historico_usuario_pedido_ativo(request):
    if request.user.is_superuser:
        return HttpResponseNotFound("Acesso Negado!")
    user = request.user.id
    pedido = Pedido.objects.all().filter(solicitante=user).filter(situacao_pedido=1)
    return render(request, 'servico/historico.html', {
        'pedido': pedido,
    })

@login_required
def historico_usuario_pedido_finalizado(request):
    if request.user.is_superuser:
        return HttpResponseNotFound("Acesso Negado!")
    user = request.user.id
    pedido = Pedido.objects.all().filter(solicitante=user).filter(situacao_pedido=2)
    return render(request, 'servico/historico.html', {
        'pedido': pedido,
    })

@login_required
def historico_usuario_pedido_cancelado(request):
    if request.user.is_superuser:
        return HttpResponseNotFound("Acesso Negado!")
    user = request.user.id
    pedido = Pedido.objects.all().filter(solicitante=user).filter(situacao_pedido=3)
    return render(request, 'servico/historico.html', {
        'pedido': pedido,
    })



@login_required
def status_usuario(request):
    if request.user.is_superuser:
        return HttpResponseNotFound("Acesso Negado!")
    user = request.user.id
    status = Status.objects.all().filter(pedido__solicitante=user)
   
    return render(request, 'servico/status.html', { 'status': status,})

@login_required
def buscar_por_status(request):
    if request.user.is_superuser:
        return HttpResponseNotFound("Acesso Negado!")
    user = request.user.id
    termo = request.GET.get('termo', None)
    status = Status.objects.all()
    if termo:
        status = Status.objects.all().filter(pedido__solicitante=user)
        status = status.filter(pedido_id__exact=termo)
        if not status:
            return render(request, 'servico/buscar_por_status_not_found.html')
    if not termo:
        return render(request, 'servico/buscar_por_status_not_found.html')
    return render(
        request, 'servico/buscar_por_status.html', {
            'status': status,
        }
    )

    return render(request, 'servico/buscar_por_status.html')


