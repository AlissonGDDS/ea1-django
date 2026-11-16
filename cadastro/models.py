from django.db import models


class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo


class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    cursos = models.ManyToManyField(Curso, blank=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    validade = models.DateField()

    def __str__(self):
        return self.nome