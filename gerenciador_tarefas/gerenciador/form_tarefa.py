from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    # criar uma classe que cria e opera um formulário já baseado no modelo
    # assim devia resolver os erros e trabalho de criar o form no html direto

    class Meta:
        #classe de configuração, pra dizer qual modelo usar e o que aparece no forms
        model = Tarefa
        fields = ['nome', 'tipo', 'descricao']