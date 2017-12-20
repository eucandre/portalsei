from django.shortcuts import render
from .models import*

def Apresentacao(request):
	"""
		Este metodo sera o responsavel pela Apresentacao do sistema.
		Aqui as variaveis do sistema serao chamadas para exibir os seus resultados.
	"""

	obj_noticias = Noticias.objects.all()
	if len(obj_noticias)>0:
		return render (request, 'apps/index.html',{"noticias":obj_noticias})
	else:
		return render (request, 'apps/index.html')
