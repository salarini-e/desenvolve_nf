from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cursos.urls')),
    path('', include('autenticacao.urls')),
    path('administracao/', include('administracao.urls')),
    path('palestras/', include(('palestras.urls', 'palestras'), namespace ='palestras')),
    path('eventos/', include(('eventos.urls', 'eventos'), namespace ='eventos')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)