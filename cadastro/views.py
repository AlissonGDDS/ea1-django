from django.shortcuts import render, redirect
from .models import Aluno, Curso, Produto
from .forms import ProdutoForm


def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'cadastro/alunos.html', {'alunos': alunos})


def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cadastro/cursos.html', {'cursos': cursos})


def produto_new(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto_new')
    else:
        form = ProdutoForm()
    return render(request, 'cadastro/produto_form.html', {'form': form})


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'cadastro/produtos.html', {'produtos': produtos})