from django.contrib import admin
from .models import Aluno, Curso, Produto

admin.site.register(Aluno)
admin.site.register(Curso)
admin.site.register(Produto)