from django.contrib import admin
from .models import *

admin.site.register(Universidade)
admin.site.register(Curso)
admin.site.register(Secretaria)
admin.site.register(Vagas)
admin.site.register(Supervisor)
admin.site.register(Estudante)
admin.site.register(Estudante_Vaga)
admin.site.register(Processo)
admin.site.register(Responsavel_Universidade)
admin.site.register(Locais_de_Estagio)
admin.site.register(Historico_Processo)