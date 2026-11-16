from django.shortcuts import render
from .models import Aluno, Curso


def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'cadastro/alunos.html', {'alunos': alunos})


def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cadastro/cursos.html', {'cursos': cursos})