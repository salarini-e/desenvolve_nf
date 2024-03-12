from django.contrib import admin
from .models import *
# Este app é para registrar e monitorar comportamentos suspeitos.
@admin.register(TentativaBurla)
class TentativaBurlaAdmin(admin.ModelAdmin):
    list_display = ['user', 'local_deteccao', 'ip_address', 'data_tentativa']
    list_filter = ['local_deteccao', 'data_tentativa']
    search_fields = ['user__username', 'ip_address', 'informacoes_adicionais']
    readonly_fields = ['data_tentativa']

@admin.register(ErroPrevisto)
class ErroPrevistoAdmin(admin.ModelAdmin):
    list_display = ['user', 'local_deteccao', 'ip_address', 'data_tentativa']
    list_filter = ['local_deteccao', 'data_tentativa']
    search_fields = ['user__username', 'ip_address', 'informacoes_adicionais']
    readonly_fields = ['data_tentativa']