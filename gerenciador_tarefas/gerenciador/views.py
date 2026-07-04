from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def home(request):
    #return HttpResponse('Página inicial do gerenciador de tarefas')
    contexto = {
        'usuario': 'teste',
        'notificacoes': 4,
        'frutas': ['Maçã', 'Banana', 'Laranja', 'maracujá'],
    }
    # O Django vai automaticamente procurar esse HTML na sua pasta 'jinja2/'
    return render(request, 'minha_pagina.html', contexto)

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
                return redirect('home')
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form': form})

def logout_page(request):
    logout(request)
    return redirect('login')
