from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from votar.models import Alunos
from votar import models
# Create your views here.

candidato1 = models.candidato1
candidato2 = models.candidato2
candidato3 = models.candidato3
candidato4 = models.candidato4
candidato5 = models.candidato5

candidato6 = models.candidato6
candidato7 = models.candidato7
candidato8 = models.candidato8
candidato9 = models.candidato9
candidato10 = models.candidato10

def homepage_redirect(request):
  return HttpResponseRedirect('votar/')

def votar(request):

  context = {
    'candidato1': candidato1,
    'candidato2': candidato2,
    'candidato3': candidato3,
    'candidato4': candidato4,
    'candidato5': candidato5,
    'candidato6': candidato6,
    'candidato7': candidato7,
    'candidato8': candidato8,
    'candidato9': candidato9,
    'candidato10': candidato10,
  }

  if request.method == 'POST':
    global matriculaForm
    matriculaForm = request.POST['matricula']
    voto_rei = request.POST['voto_rei']
    voto_rainha = request.POST['voto_rainha']

    if (matriculaForm == ''):
      messages.error(request, 'Matrícula vazia!')
      return render (request, 'votar.html', context)
    elif (voto_rei == '0') or (voto_rainha == '0'):
      messages.error(request, 'Selecione um candidato!')
      return render (request, 'votar.html', context)
    elif (Alunos.objects.filter(matricula=matriculaForm)) and ((Alunos.objects.get(matricula=matriculaForm).statusvoto) == 'N'):
      nome = Alunos.objects.get(matricula=matriculaForm).nome
      computar_voto = Alunos(matricula=matriculaForm, nome=nome, voto_rei=voto_rei, voto_rainha=voto_rainha, statusvoto='S')
      computar_voto.save()
      return HttpResponseRedirect('/resultado/')
    elif (Alunos.objects.filter(matricula=matriculaForm)) and ((Alunos.objects.get(matricula=matriculaForm).statusvoto) == 'S'):
      messages.error(request, 'Você já votou!')
      return render (request, 'votar.html', context)
    else:
      messages.error(request, 'Matrícula incorreta!')
      return render(request, 'votar.html', context)

  return render(request, 'votar.html', context)

def resultado(request):

  global context

  vC1 = Alunos.objects.filter(voto_rei=1).count()
  vC2 = Alunos.objects.filter(voto_rei=2).count()
  vC3 = Alunos.objects.filter(voto_rei=3).count()
  vC4 = Alunos.objects.filter(voto_rei=4).count()
  vC5 = Alunos.objects.filter(voto_rei=5).count()

  vC6 = Alunos.objects.filter(voto_rainha=6).count()
  vC7 = Alunos.objects.filter(voto_rainha=7).count()
  vC8 = Alunos.objects.filter(voto_rainha=8).count()
  vC9 = Alunos.objects.filter(voto_rainha=9).count()
  vC10 = Alunos.objects.filter(voto_rainha=10).count()

  votosTotais = Alunos.objects.filter(statusvoto='S').count()

  podioReis = {candidato1: vC1, candidato2: vC2, candidato3: vC3, candidato4: vC4, candidato5: vC5}
  podioRainhas = {candidato6: vC6, candidato7: vC7, candidato8: vC8, candidato9: vC9, candidato10: vC10}

  fPodioReis = []
  fPodioReisPct = []

  fPodioRainhas = []
  fPodioRainhasPct = []

  for x in range(3):
    posicaoHA = max(podioReis, key=podioReis.get)
    posicaoHB = podioReis[posicaoHA]
    posicaoHPct = str(((posicaoHB) * 100) / (votosTotais)) + '%'
    fPodioReis.append(posicaoHA)
    fPodioReisPct.append(posicaoHPct)
    podioReis.pop(posicaoHA)

  for y in range(3):
    posicaoMA = max(podioRainhas, key=podioRainhas.get)
    posicaoMB = podioRainhas[posicaoMA]
    posicaoMPct = str(((posicaoMB) * 100) / (votosTotais)) + '%'
    fPodioRainhas.append(posicaoMA)
    fPodioRainhasPct.append(posicaoMPct)
    podioRainhas.pop(posicaoMA)

  context = {
  'primeiroRei': fPodioReis[0],
  'primeiroReiPorcentagem': fPodioReisPct[0],
  'segundoRei': fPodioReis[1],
  'segundoReiPorcentagem': fPodioReisPct[1],
  'terceiroRei': fPodioReis[2],
  'terceiroReiPorcentagem': fPodioReisPct[2],
  'primeiraRainha': fPodioRainhas[0],
  'primeiraRainhaPorcentagem': fPodioRainhasPct[0],
  'segundaRainha': fPodioRainhas[1],
  'segundaRainhaPorcentagem': fPodioRainhasPct[1],
  'terceiraRainha': fPodioRainhas[2],
  'terceiraRainhaPorcentagem': fPodioRainhasPct[2],
  }

  return render(request, 'resultado.html', context)

def candidatos(request):
  return render(request, 'candidatos.html')