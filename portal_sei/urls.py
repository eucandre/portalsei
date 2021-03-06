
from django.conf.urls import *
from django.contrib import admin
from app_documentos.views import *
from app_documentos.insere import *
from app_documentos.edita import *
from app_documentos.deleta import *
from app_documentos.item import *
from django.conf import settings
from django.conf.urls.static import static
from app_documentos.api import *
from capacitacoes.views import *
from tastypie.api import Api
from app_documentos.serializers import *
from app_usuario.views import *
from app_FAQ.views import *
from app_manuais.views import *
from app_guia_implantacao.views import *

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
    url(r'^InsereFAQ',Cria_FAQ),
    url(r'^listaFAQ',listaFAQ),
    url(r'^EditaFAQ',Edita_FAQ),
    url(r'^itemFAQ/(?P<nr_item>\d+)/$',itemFAQ),
    url(r'^InsereCapacitacao', InsereCapacitacao),
    url(r'^EditarCapacitacao/(?P<nr_item>\d+)/$',editaCapacitacao),
    url(r'^DeletaCapacitacao/(?P<nr_item>\d+)/$',CapacitacaoDelete),
    url(r'^InsereCategoria',InsereCategoria),
    url(r'^InsereTag',InsereTag),
    url(r'^lista_documentos', lista_documentos),
    url(r'^historico', historico),
    url(r'^lista_capacitacoes', lista_capacitacoes),
    url(r'^lista_noticias', lista_noticias),
    url(r'^noticias/(?P<nr_item>\d+)/$',itemNoticia),
    url(r'^EditarDocumento/(?P<nr_item>\d+)/$',EditaDocumento),
    url(r'^EditarCategoria/(?P<nr_item>\d+)/$',EditaCategoria),
    url(r'^Delete_Documento/(?P<nr_item>\d+)/$', DocumentoDelete),
    url(r'^login/$', user_login),
    url(r'^EditaNoticia/(?P<nr_item>\d+)/$',EditaNoticia),
    
    url(r'^CriaManual',cria_manual),
    url(r'^listaManuais',lista_manuais),

    url(r'^Cria_Tutorial',Cria_Tutorial),
    url(r'^Lista_tutorial',Lista_tutorial),
        url(r'^item_tutorial/(?P<nr_item>\d+)/$',item_tutorial),
    url(r'^AcessoAoSei',AcessoAoSei),
    url(r'^sobreOsei',sobreSei),
    url(r'^capacitacao',capacitacao),
    url(r'^equipe',equipe),
    url(r'^froala_editor/', include('froala_editor.urls')),
    #api
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
