from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse
from .models import Cliente
from .forms import ClienteForm


# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def login(request):
    return render(request, 'home/login.html') 

def my_logout(request):
    logout(request)
    return redirect('login')  

def cadastro(request):

    if request.method != 'POST':
        return render(request, 'home/cadastro.html')

    cpf = request.POST.get('cpf', None)
    rg = request.POST.get('rg', None)
    telefone = request.POST.get('telefone', None)
    endereco = request.POST.get('endereco', None)
    nome = request.POST.get('nome', None)
    email = request.POST.get('email', None)
    usuario = request.POST.get('usuario', None)
    senha = request.POST.get('senha', None)
    senha2 = request.POST.get('senha2', None)

    if not nome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'home/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'E-mail Inválido.')
        return render(request,'home/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'E-mail já cadastrado.')
        return render(request, 'home/cadastro.html')
    
    if len(senha) < 6:
        messages.error(request, 'Erro! a senha não pode ser menor que 6 caracteres')
        return render(request, 'home/cadastro.html')
    
    if len(usuario) < 6:
        messages.error(request, 'Usuário precisa ter 6 caracteres ou mais.')
        return render(request, 'home/cadastro.html')
    
    if senha != senha2:
        messages.error(request, 'Senhas não conferem.')
        return render(request, 'home/cadastro.html')
    
    if len(cpf) != 11:
        messages.error(request, 'CPF Inválido.')
        return render(request, 'home/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe.')
        return render(request, 'home/cadastro.html')
    

    
    user = User.objects.create_user(username=usuario, email=email, first_name=nome, password=senha)
    user.save()
    cliente = Cliente.objects.create(user=user, rg=rg, cpf=cpf, endereco=endereco, telefone=telefone, nome_cliente=nome)
    cliente.save()
    

    messages.success(request, ' Registrado com sucesso! Faça login para acessar.')
    return redirect('login')

    return render(request, 'home/cadastro.html')

 
def alterar_perfil(request):
    if request.user.is_superuser:
        user = request.user
        cliente = None
    else:
        cliente = request.user.cliente
        user = request.user
    
    if request.method == 'POST':
        form =UserChangeForm(request.POST, instance=request.user)

        if form.isvalid():
            form.save()
            return redirect('inicial')
    
    else:
        form = UserChangeForm(instance=request.user)
    
        return render(request, 'home/alterar_perfil.html', {
            'form': form,
            'user': user,
            'cliente': cliente})