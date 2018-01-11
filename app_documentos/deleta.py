from django.shortcuts import render, get_object_or_404, redirect
from app_documentos.models import *

def DocumentoDelete(request,nr_item):
   
  	doc = get_object_or_404(Documentos, pk=nr_item)
  	doc.delete()
  	return redirect("/lista_documentos/")