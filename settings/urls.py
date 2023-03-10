from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('capacitacao-profissional/', include('cursos.urls')),    
    path('casa-do-trabalhador/', include('casa_do_trabalhador.urls')),
    path('bem-estar-animal/', include('bemestaranimal.urls')),
    path('', include('autenticacao.urls')),
    path('', include('desenvolve_nf.urls')),
    path('administracao/', include('administracao.urls')),
    path('palestras/', include(('palestras.urls', 'palestras'), namespace ='palestras')),
    path('financas/', include('financas.urls')),
    path('eventos/', include('eventos.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
