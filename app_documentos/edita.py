from django.shortcuts import render
from .forms import *

def EditaTipoDocumento(request, nr_item):
	item = Documentos.objects.get(pk = nr_item)
	if request.method == 'POST':
		form  =  FormTipoDocumento(request.POST)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
	else:
		form = FormTipoDocumento(instance=item)
	return render(request, 'apps/insere_tipo_documento.html', {'form':form})

def EditaSetor(request, nr_item):
	item = Setor.objects.get(pk=nr_item)
	if request.method == 'POST':
		form  =  FormSetor(request.POST)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
	else:
		form = FormSetor(instance=item)
	return render(request, 'apps/insere_setor.html', {'form':form})	

def EditaCliente(request, nr_item):
	item = Cliente.objects.get(pk=nr_item)
	if request.method == 'POST':
		form  =  FormCliente(request.POST)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
	else:
		form = FormCliente(instance=item)
	return render(request, 'apps/insere_cliente.html', {'form':form})	

def EditaDocumento(request, nr_item):
	item = Documentos.objects.get(pk= nr_item)
	if request.method == 'POST':
		form  =  FormDocumentos(request.POST, request.FILES)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
	else:
		form = FormDocumentos(instance= item)
	return render(request, 'apps/insere_documento.html', {'form':form})		

def EditaHelpDesk(request, nr_item):
	item = Help_Desk.objects.get(pk=nr_item)
	if request.method == 'POST':
		form  =  FormHelpDesk(request.POST)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
	else:
		form = FormHelpDesk(instance=item)
	return render(request, 'apps/insere_help_desk.html', {'form':form})		
