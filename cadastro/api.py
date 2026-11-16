from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def usuarios(request):
    dados = [
        {"nome": "Carlos", "email": "carlos@email.com"},
        {"nome": "João", "email": "joao@email.com"},
    ]
    return Response(dados)