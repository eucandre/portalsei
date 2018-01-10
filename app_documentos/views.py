from django.shortcuts import render
from .models import*
from .forms import *




def Apresentacao(request):
	"""
		Este metodo sera o responsavel pela Apresentacao do sistema.
		Aqui as variaveis do sistema serao chamadas para exibir os seus resultados.
		O metodo irah retornar, para o template, os dois ultimos registros no banco fazendo uso da variavel obj_noticias
	"""

	if len(Noticias.objects.all()) == 1:	
		obj_noticias = Noticias.objects.all()[(len(Noticias.objects.all())-1):]
		if len(obj_noticias) > 0:
			return render (request, 'apps/index.html',{"noticias":obj_noticias})

	if len(Noticias.objects.all()) > 1:
		obj_noticias = Noticias.objects.all()[(len(Noticias.objects.all())-2):]
		if len(obj_noticias) > 0:
			return render (request, 'apps/index.html',{"noticias":obj_noticias})
	else:
		return render (request, 'apps/index.html')

def dashboard(request):
	return render(request, 'dashboard.html')