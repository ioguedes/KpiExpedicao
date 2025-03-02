from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Sum
from .models import Carregamento
from .forms import CarregamentoForm
from datetime import datetime

def lista_carregamentos(request):
    carregamentos = Carregamento.objects.all()
    return render(request, 'expedicao/lista_carregamentos.html', {'carregamentos': carregamentos})

def adicionar_carregamento(request):
    if request.method == "POST":
        form = CarregamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_carregamentos')
    else:
        form = CarregamentoForm()
    return render(request, 'expedicao/adicionar_carregamento.html', {'form': form})

from django.shortcuts import render
from .models import Carregamento

def relatorio_analitico(request):
    # Filtros de data (início e fim)
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')

    # Filtros por separador e conferente
    separador = request.GET.get('separador')
    conferente = request.GET.get('conferente')

    # Consulta inicial
    carregamentos = Carregamento.objects.all()

    # Aplicar filtros de data
    if data_inicio and data_fim:
        data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d').date()
        data_fim = datetime.strptime(data_fim, '%Y-%m-%d').date()
        carregamentos = carregamentos.filter(data_carregamento__range=[data_inicio, data_fim])

    # Aplicar filtro por separador
    if separador:
        carregamentos = carregamentos.filter(separador=separador)

    # Aplicar filtro por conferente
    if conferente:
        carregamentos = carregamentos.filter(conferente=conferente)

    # Total de pesos carregados e descarregados por dia
    pesos_por_dia = carregamentos.values('data_carregamento').annotate(
        total_carregado=Sum('peso', filter=Q(tipo='carregamento')),
        total_descarregado=Sum('peso', filter=Q(tipo='descarregamento'))
    ).order_by('data_carregamento')

    # Desempenho individual de conferentes e separadores
    desempenho_conferentes = carregamentos.values('conferente').annotate(
        total_peso=Sum('peso')
    ).order_by('-total_peso')

    desempenho_separadores = carregamentos.values('separador').annotate(
        total_peso=Sum('peso')
    ).order_by('-total_peso')

    # Lista de separadores e conferentes para os filtros
    separadores = Carregamento.objects.values('separador').distinct()
    conferentes = Carregamento.objects.values('conferente').distinct()

    return render(request, 'expedicao/relatorio_analitico.html', {
        'pesos_por_dia': pesos_por_dia,
        'desempenho_conferentes': desempenho_conferentes,
        'desempenho_separadores': desempenho_separadores,
        'data_inicio': data_inicio,
        'data_fim': data_fim,
        'separadores': separadores,
        'conferentes': conferentes,
        'separador': separador,
        'conferente': conferente,
    })


def detalhes_carregamento(request, id):
    carregamento = get_object_or_404(Carregamento, id=id)
    return render(request, 'expedicao/detalhes_carregamento.html', {'carregamento': carregamento})


