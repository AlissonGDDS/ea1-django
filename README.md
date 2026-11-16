# Cadastro de Alunos e Cursos (Django)

Projeto da 1ª Experiência de Aprendizagem (EA1): um sistema simples em Django para cadastrar alunos e cursos, gerenciar os dados pelo Django Admin e exibi-los em páginas web.

## O que o sistema faz

- Cadastra **alunos** (nome, sobrenome e e-mail).
- Cadastra **cursos** (título e descrição).
- Um aluno pode estar matriculado em **vários cursos** (relação muitos para muitos).
- Gerenciamento de tudo pelo **Django Admin**.
- Páginas web que listam os alunos e os cursos cadastrados.

## Tecnologias

- Python
- Django
- SQLite (banco padrão do Django)

## Como rodar o projeto

1. Clone o repositório e entre na pasta:

```
git clone https://github.com/AlissonGDDS/ea1-django.git
cd ea1-django
```

2. Crie e ative o ambiente virtual (Windows / PowerShell):

```
python -m venv venv
.\venv\Scripts\activate
```

No Linux ou Mac, a ativação é `source venv/bin/activate`.

3. Instale o Django:

```
pip install django
```

4. Crie o banco de dados:

```
python manage.py migrate
```

5. Crie um usuário administrador:

```
python manage.py createsuperuser
```

6. Inicie o servidor:

```
python manage.py runserver
```

## Endereços

| Endereço | O que mostra |
|---|---|
| `http://127.0.0.1:8000/admin/` | Django Admin (cadastro de alunos e cursos) |
| `http://127.0.0.1:8000/alunos/` | Lista de alunos e seus cursos |
| `http://127.0.0.1:8000/cursos/` | Lista de cursos |

## Estrutura do projeto

```
escola/      configurações do projeto (settings.py, urls.py)
cadastro/    app principal
  models.py      modelos Aluno e Curso
  admin.py       registro dos modelos no admin
  views.py       views que listam alunos e cursos
  urls.py        rotas do app
  templates/     páginas HTML (alunos.html e cursos.html)
manage.py    utilitário de comandos do Django
```

## Autor

Alisson Germano