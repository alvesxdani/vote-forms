from django.shortcuts import render
from vote.models import Vote

# Create your views here.
def renderIndex(request):
  return render(request, 'index.html')

def render_votacao_enviada(request):
    votacao_dados = {
        'nome': request.POST.get('nome'),
        'turma': request.POST.get('turma'),
        'flor': request.POST.get('flor')
    }

    result = Vote(**votacao_dados)
    result.save()
    return render(request, 'votacao_enviada.html', {'nome': result.nome, 'turma': result.turma, 'flor': result.flor})