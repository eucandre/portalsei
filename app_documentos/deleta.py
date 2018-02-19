from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from app_documentos.models import *

@login_required
def DocumentoDelete(request,nr_item):
   
  	doc = get_object_or_404(Documentos, pk=nr_item)
  	doc.delete()
  	return redirect("/lista_documentos/")

@login_required
def CategoriaDelete(request, nr_item):

	categoria = get_object_or_404(Categoria_noticia, pk=nr_item)
	categoria.delete()
	return redirect("/")