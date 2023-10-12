from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    # Salvar os dados da tela para o banco de dados.
    novo_Usuario = Usuario()
    novo_Usuario.nome = request.POST.get('nome')
    novo_Usuario.idade = request.POST.get('idade')
    novo_Usuario.save()
    # Exibir todos  os Usuários já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    # Retornar os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios) 
