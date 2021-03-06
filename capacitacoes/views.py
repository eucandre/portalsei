from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import *
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

@login_required(login_url='/login/')
def InsereCapacitacao(request):
	if request.method == 'POST':
		form = FormEventos(request.POST, request.FILES)
		if form.is_valid():
			item = form.save(commit=False)
			item.user = request.user
			item.save()
	else:
		form = FormEventos()
	return render(request, 'app_capacitacoes/insere_capacitacao.html',{'form':form})

@login_required
def editaCapacitacao(request, nr_item):
	item = Evento.objects.get(pk =  nr_item)
	if request.method == 'POST':
		form = FormEventos(request.POST, request.FILES,instance=item)
		if form.is_valid():
			item = form.save(commit=False)
			item.user = request.user
			item.save()
	else:
		form = FormEventos(instance=item)
	return render(request, 'app_capacitacoes/insere_capacitacao.html',{'form':form})

@login_required
def CapacitacaoDelete(request,nr_item):
   
  	doc = get_object_or_404(Evento, pk=nr_item)
  	doc.delete()
  	return redirect("/lista_capacitacoes/")


def lista_capacitacoes(request):
	lista = Evento.objects.all()
	page = request.GET.get("page",1)
	paginator = Paginator(lista, 3)
	try:
		# page = int(request.Get.get("page",1))
		p_lista = paginator.page(page)
	except PageNotAnInteger:
		p_lista = paginator.page(1)
	except EmptyPage:
		p_lista = paginator.page(paginator.num_pages)
	return render(request, 'app_capacitacoes/lista_capacitacoes.html',{'lista':p_lista})