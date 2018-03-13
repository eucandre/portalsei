# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import *

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import *


def Cria_FAQ(request):
	if request.method == 'POST':
		form = FormDuvidas(request.POST)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
	else:
		form = FormDuvidas()
	return render(request, "app_faq/insere_faq.html",{"form":form})


def Edita_FAQ(request,nr_item):
	item = Duvidas.objects.get(pk= nr_item)
	if request.method == 'POST':
		form = FormDuvidas(request.POST, instance=item)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
	else:
		form = FormDuvidas(instance=item)
	return render(request, "app_faq/insere_faq.html",{"form":form})

def itemFAQ(request, nr_item):
	try:
		item = Duvidas.objects.get(pk=nr_item)
	except:
		raise Http404('Sem Registro!')
	return render(request, "app_faq/item_duvidas.html", {'item': item})


def listaFAQ(request):

	lista = Duvidas.objects.all()
	page = request.GET.get("page",1)
	paginator = Paginator(lista, 3)
	try:
		# page = int(request.Get.get("page",1))
		p_lista = paginator.page(page)
	except PageNotAnInteger:
		p_lista = paginator.page(1)
	except EmptyPage:
		p_lista = paginator.page(paginator.num_pages)
	return render(request, 'lista_duvidas.html',{'lista':p_lista})
