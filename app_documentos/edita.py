from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *


@login_required
def EditaTipoDocumento(request, nr_item):
	item = Documentos.objects.get(pk = nr_item)
	if request.method == 'POST':
		form  =  FormTipoDocumento(request.POST, instance=item)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
			return redirect("/lista_documentos/")
	else:
		form = FormTipoDocumento(instance=item)
	return render(request, 'apps/insere_tipo_documento.html', {'form':form})


@login_required
def EditaSetor(request, nr_item):
	item = Setor.objects.get(pk=nr_item)
	if request.method == 'POST':
		form  =  FormSetor(request.POST, instance=item)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
			return redirect("/lista_documentos/")
	else:
		form = FormSetor(instance=item)
	return render(request, 'apps/insere_setor.html', {'form':form})	


@login_required
def EditaCliente(request, nr_item):
	item = Cliente.objects.get(pk=nr_item)
	if request.method == 'POST':
		form  =  FormCliente(request.POST, instance=item)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
			return redirect("/lista_documentos/")
	else:
		form = FormCliente(instance=item)
	return render(request, 'apps/insere_cliente.html', {'form':form})	


@login_required
def EditaDocumento(request, nr_item):
	item = Documentos.objects.get(pk= nr_item)
	if request.method == 'POST':
		form  =  FormDocumentos(request.POST, request.FILES, instance=item)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
			return redirect("/lista_documentos/")
	else:
		form = FormDocumentos(instance= item)
	return render(request, 'apps/insere_documento.html', {'form':form})		


@login_required
def EditaHelpDesk(request, nr_item):
	item = Help_Desk.objects.get(pk=nr_item)
	if request.method == 'POST':
		form  =  FormHelpDesk(request.POST,instance=item)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
			return redirect("/lista_documentos/")
	else:
		form = FormHelpDesk(instance=item)
	return render(request, 'apps/insere_help_desk.html', {'form':form})		


@login_required
def EditaNoticia(request, nr_item):
	item = Noticias.objects.get(pk=nr_item)
	if request.method == 'POST':
		form  =  FormNoticias(request.POST,instance=item)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
			return redirect("/lista_documentos/")
	else:
		form = FormNoticias(instance=item)
	return render(request, 'apps/insere_noticia.html', {'form':form})		

@login_required
def EditaCategoria(request, nr_item):
	item = Categoria_noticia.objects.get(pk= nr_item)
	if request.method=='POST':
		form = FormCategoria(request.POST,instance=item)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
			return redirect("/lista_documentos/")
	else:
		form = FormCategoria()
	return render(request, 'apps/insere_categoria.html',{'form':form})