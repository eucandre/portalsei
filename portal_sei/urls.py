
from django.conf.urls import *
from django.contrib import admin
from app_documentos.views import *
from app_documentos.insere import *
from app_documentos.edita import *
from app_documentos.deleta import *
from django.conf import settings
from django.conf.urls.static import static
from app_documentos.api import *
from capacitacoes.views import *
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(TagResourse())
tags_resurse = TagResourse()


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
    url(r'^InsereCapacitacao', InsereCapacitacao),
    url(r'^lista_documentos', lista_documentos),
    url(r'^lista_noticias', lista_noticias),
    url(r'^EditarDocumento/(?P<nr_item>\d+)/$',EditaDocumento),
    url(r'^Delete_Documento/(?P<nr_item>\d+)/$', DocumentoDelete),

    url(r'^EditaNoticia/(?P<nr_item>\d+)/$',EditaNoticia),
    

    url(r'^froala_editor/', include('froala_editor.urls')),
    #api
    url(r'^api/',include(tags_resurse.urls)),    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
