# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import *

from django.core.paginator import *
from django.contrib.auth.decorators import login_required

def cria_manual(request):
	if request.method == 'POST':
		form  =  FormManual(request.POST)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
	else:
		form = FormManual()
	return render(request, 'app_manual/insere_manual.html', {'form':form})

def lista_manuais(request):

	lista = Manual.objects.all()
	page = request.GET.get("page",1)
	paginator = Paginator(lista, 3)
	try:
		# page = int(request.Get.get("page",1))
		p_lista = paginator.page(page)
	except PageNotAnInteger:
		p_lista = paginator.page(1)
	except EmptyPage:
		p_lista = paginator.page(paginator.num_pages)
	return render(request, 'app_manual/lista_manuais.html',{'lista':p_lista})	