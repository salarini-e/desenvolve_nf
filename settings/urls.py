from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('atualizacao/', include('financas_recadastramento.urls')),
    path('', include('autenticacao.urls')),
    path('', include('desenvolve_nf.urls')),
    path('', include('formularios.urls')),
    path('api/', include('api.urls')),
    path('ciencia-e-tecnologia/', include('cursos.urls')),    
    path('chat/', include('chat.urls')),
    path('sala-do-empreendedor/', include('sala_do_empreendedor.urls')),
    path('sala-do-empreendedor/', include('cursos_empresariais.urls')),
    path('sala-do-empreendedor/', include('cursos_profissionais.urls')),
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
    path('senha-facil/', include('senhas_facil.urls')),
    path('dados-abertos/', include('painel_de_dados.urls')),
    path('administracao/', include('administracao.urls')),    
    path('django/', admin.site.urls),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
