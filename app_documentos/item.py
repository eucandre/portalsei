from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *

def itemNoticia(request, nr_item):
    try:
        titulo = Noticias.objects.all().values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('titulo')
        #titulo = Noticias.objects.get(pk = nr_item)
        categoria = Noticias.objects.all().values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('categoria_da_noticia')
        data = Noticias.objects.all().values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('data_publicacao')
        destaque = Noticias.objects.all().values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('destaque')
        publicado = Noticias.objects.all().values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('publicado')
        imagem = Noticias.objects.all().values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('imagem')
        video = Noticias.objects.all().values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('video')
        credito_midia_imagem = Noticias.objects.all().values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('credito_midia_imagem')
        legenda_da_imagem = Noticias.objects.all().values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('legenda_da_imagem')
        credito_midia_video = Noticias.objects.all().values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('credito_midia_video')
        legenda_do_video = Noticias.objects.all().values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('legenda_do_video')
        documentos_complementares = Noticias.objects.all().values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('documentos_complementares')
        chapeu = Noticias.objects.all().values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('chapeu')
        bigode = Noticias.objects.all().values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('bigode')
        reporter = Noticias.objects.all().values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('reporter')
        tags_lista = Noticias.objects.all().values()[0]#values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('tags_lista')
        nota = Noticias.objects.all().values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('nota')
        user = Noticias.objects.all().values()[len(Noticias.objects.all())-len(Noticias.objects.all())].get('user')
    except Noticias.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "app_capacitacoes/item_noticias.html", {'titulo': titulo, 'categoria':categoria, 'data':data
    	,'destaque':destaque,'publicado':publicado, 'imagem':imagem,'video':video, 'credito_midia_imagem':credito_midia_imagem,
    	'credito_midia_video':credito_midia_video,'legenda_da_imagem':legenda_da_imagem,'legenda_do_video':legenda_do_video,
    	'documentos_complementares':documentos_complementares,'chapeu':chapeu, 'bigode':bigode, 'reporter':reporter,
    	 'tags_lista':tags_lista, 'conteudo':nota})