
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

    url(r'^lista_documentos', lista_documentos),
    url(r'^Editar/(?P<nr_item>\d+)/$',EditaDocumento),
    url(r'^Delete/(?P<nr_item>\d+)/$', DocumentoDelete),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
