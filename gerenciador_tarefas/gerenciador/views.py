from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from gerenciador.form_tarefa import TarefaForm
from gerenciador.models import Tarefa


def home(request):
    #return HttpResponse('Página inicial do gerenciador de tarefas')

    return render(request, 'inicio.html')

def base(request):
    return render(request, 'base.html')

def inicio(request):
    return render(request, 'inicio.html')

def cadastro(request):
    if request.method != 'POST':
        form = UserCreationForm()
        return render(request, 'cadastro.html', {'form': form})

    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user) 
                return redirect('perfil')
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form': form})

def logout_page(request):
    logout(request)
    return redirect('login')

# usar essa tag para garantir que apenas usuários logados tenham acesso
@login_required(login_url='login')
def perfil(request):

    tarefas = Tarefa.objects.filter(usuario=request.user)

    context = {
        'usuario': request.user,
        'tarefas': tarefas
    }
    return render(request, 'perfil.html', context)

@login_required(login_url='login')
def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user
            tarefa.save()
            return redirect('perfil')
    else:
        form = TarefaForm()
    
    return render(request, 'criar_tarefa.html', {'form': form})
