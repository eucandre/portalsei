
from django.conf.urls import url
from django.contrib import admin
from app_documentos.views import *
from app_documentos.insere import *
from app_documentos.edita import *
from app_documentos.deleta import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Apresentacao),
    url(r'^dashboard',dashboard),
    url(r'^InsereTipoDocumento',InsereTipoDocumento), 
    url(r'^InsereSetor',InsereSetor),
    url(r'^InsereCliente',InsereCliente),
    url(r'^InsereDocumento',InsereDocumento),
    url(r'^InsereHelpDesk',InsereHelpDesk),
    url(r'^InsereNoticia',InsereNoticia),

    url(r'^lista_documentos', lista_documentos),
    url(r'^EditarDocumento/(?P<nr_item>\d+)/$',EditaDocumento),
    url(r'^Delete_Documento/(?P<nr_item>\d+)/$', DocumentoDelete),

    url(r'^EditaNoticia/(?P<nr_item>\d+)/$',EditaNoticia),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
