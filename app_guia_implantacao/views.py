# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import *

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import *


def Cria_Tutorial(request):
	if request.method == 'POST':
		form = Formtutorial(request.POST)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
	else:
		form = Formtutorial()
	return render(request, "Guia_Implantacao/insere_tutoria.html",{"form":form})

def Lista_tutorial(request):
	lista = Tutorial.objects.all()
	page = request.GET.get("page",1)
	paginator = Paginator(lista, 3)
	try:
		# page = int(request.Get.get("page",1))
		p_lista = paginator.page(page)
	except PageNotAnInteger:
		p_lista = paginator.page(1)
	except EmptyPage:
		p_lista = paginator.page(paginator.num_pages)
	return render(request, 'Guia_Implantacao/Guia_implantacao.html',{'lista':p_lista})

def item_tutorial(request, nr_item):
	try:
		item = Tutorial.objects.get(pk=nr_item)
	except:
		raise Http404('Sem Registro!')
	return render(request, "Guia_implantacao/item_guia_implantacao.html", {'item': item})


