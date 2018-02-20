from django.shortcuts import render
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def InsereTipoDocumento(request):
	if request.method == 'POST':
		form  =  FormTipoDocumento(request.POST)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
	else:
		form = FormTipoDocumento()
	return render(request, 'apps/insere_tipo_documento.html', {'form':form})

@login_required
def InsereSetor(request):
	if request.method == 'POST':
		form  =  FormSetor(request.POST)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
	else:
		form = FormSetor()
	return render(request, 'apps/insere_setor.html', {'form':form})	

@login_required
def InsereCliente(request):
	if request.method == 'POST':
		form  =  FormCliente(request.POST)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
	else:
		form = FormCliente()
	return render(request, 'apps/insere_cliente.html', {'form':form})	

@login_required
def InsereDocumento(request):
	if request.method == 'POST':
		form  =  FormDocumentos(request.POST, request.FILES)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
	else:
		form = FormDocumentos()
	return render(request, 'apps/insere_documento.html', {'form':form})		

@login_required
def InsereHelpDesk(request):
	if request.method == 'POST':
		form  =  FormHelpDesk(request.POST)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
	else:
		form = FormHelpDesk()
	return render(request, 'apps/insere_help_desk.html', {'form':form})		

@login_required
def InsereNoticia(request):
	item  = Tag.objects.all()
	if request.method == 'POST':
		form  =  FormNoticias(request.POST, request.FILES)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
	else:
		form = FormNoticias()
	return render(request, 'apps/insere_noticia.html', {'form':form, 'tags':item})		

@login_required
def InsereCategoria(request):
	if request.method=='POST':
		form = FormCategoria(request.POST)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
	else:
		form = FormCategoria()
	return render(request, 'apps/insere_categoria.html',{'form':form})

def InsereTag(request):
	if request.method=='POST':
		form = FormTag(request.POST)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
	else:
		form = FormTag()
	return render(request, 'apps/insere_tag.html',{'form':form})
