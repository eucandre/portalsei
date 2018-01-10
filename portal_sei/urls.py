
from django.conf.urls import url
from django.contrib import admin
from app_documentos.views import *
from app_documentos.insere import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Apresentacao),
    url(r'^InsereTipoDocumento',InsereTipoDocumento), 
    url(r'^InsereSetor',InsereSetor),
    url(r'^InsereCliente',InsereCliente),
    url(r'^InsereDocumento',InsereDocumento),
    url(r'^InsereHelpDesk',InsereHelpDesk),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
