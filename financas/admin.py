from django.contrib import admin
from .models import *

# admin.site.register(Conselheiros)
# admin.site.register(Pauta_de_Julgamento)
# admin.site.register(Sumulas)
# admin.site.register(Acordao)
# admin.site.register(Ata)
# admin.site.register(Voto_Relator)
# admin.site.register(Data_Reunião)

@admin.register(Classe_Formulario)
class ClasseFormularioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'div_id', 'user_inclusao', 'dt_inclusao')
    search_fields = ('nome', 'div_id')
    list_filter = ('dt_inclusao', 'user_inclusao')

@admin.register(Formularios)
class FormulariosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'classe', 'user_inclusao', 'dt_inclusao')
    search_fields = ('titulo', 'classe__nome')
    list_filter = ('dt_inclusao', 'user_inclusao')
