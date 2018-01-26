from django.shortcuts import render

from .forms import *

def InsereCapacitacao(request):
	if request.method == 'post':
		form = FormEventos(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	else:
		form = FormEventos()
	return render(request, 'app_capacitacoes/insere_capacitacao.html',{'form':form})
