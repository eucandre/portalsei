from django.shortcuts import render
from django.core.paginator import *
from django.http import *
from .models import *
from .forms import *


def Apresentacao(request):
	"""
		Este metodo sera o responsavel pela Apresentacao do sistema.
		Aqui as variaveis do sistema serao chamadas para exibir os seus resultados.
		O metodo irah retornar, para o template, os dois ultimos registros no banco fazendo uso da variavel obj_noticias
	"""

	if len(Noticias.objects.all()) == 1:	
		obj_noticias = Noticias.objects.all()[(len(Noticias.objects.all())-1):]
		img  = obj_noticias[0].values().get('imagem')

		if len(obj_noticias) > 0:
			return render (request, 'apps/index.html',{"noticias":obj_noticias})
			
	if len(Noticias.objects.all()) > 1:
		obj_noticias = Noticias.objects.all()[(len(Noticias.objects.all())-2):]
		img1 = obj_noticias.values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('imagem')
		titulo1 = obj_noticias.values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('titulo')

		img2 = obj_noticias.values()[len(Noticias.objects.all())-(len(Noticias.objects.all())-1)].get('imagem')
		titulo2 =obj_noticias.values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('titulo')
		if len(obj_noticias) > 0:
			return render (request, 'apps/index.html',{"noticias":obj_noticias, 'imagem1':img1,"titulo1":titulo1, 'imagem2':img2, 
				"titulo2":titulo2 })
	else:
		tamanho = 0
		return render (request, 'apps/index.html', {"vazio":tamanho})

def dashboard(request):
	return render(request, 'apps/index_dashboard.html')


def lista_documentos(request):

	lista = Documentos.objects.all()
	page = request.GET.get("page",1)
	paginator = Paginator(lista, 3)
	try:
		# page = int(request.Get.get("page",1))
		p_lista = paginator.page(page)
	except PageNotAnInteger:
		p_lista = paginator.page(1)
	except EmptyPage:
		p_lista = paginator.page(paginator.num_pages)
	return render(request, 'apps/lista_documentos.html',{'lista':p_lista})