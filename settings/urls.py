from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('autenticacao.urls')),
    path('', include('desenvolve_nf.urls')),
    path('api/', include('api.urls')),
    path('ciencia-e-tecnologia/', include('cursos.urls')),
    # path('capacitacao-profissional/palestras/', include(('palestras.urls', 'palestras'), namespace ='palestras')),
    path('chat/', include('chat.urls')),
    path('sala-do-empreendedor/', include('sala_do_empreendedor.urls')),
    path('sala-do-empreendedor/', include('cursos_empresariais.urls')),
    path('financas/', include('financas.urls')),
    path('eventos/', include('eventos.urls')),

    path('bem-estar-animal/', include('bemestaranimal.urls')),
    path('servicos/iluminacao/', include('iluminacao.urls')),
    path('servicos/cevest/', include('cevest_os.urls')),
    path('servicos/dev/', include('chamados_dev.urls')),
    path('almoxarifado/', include('almoxarifado.urls')),
    path('cevest/almoxarifado/', include('cevest_almoxarifado.urls')),
    path('estagio/', include('estagio.urls')),
    path('newsletter/', include('newsletter.urls')),

    path('administracao/', include('administracao.urls')),    
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
