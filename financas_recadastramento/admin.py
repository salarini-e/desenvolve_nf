from django.contrib import admin
from .models import PessoaRecadastramento, Processo, Inscricao, Servidor_Recadastramento

admin.site.register(PessoaRecadastramento)
admin.site.register(Processo)
admin.site.register(Inscricao)

@admin.register(Servidor_Recadastramento)
class ServidorRecadastramentoAdmin(admin.ModelAdmin):
    list_display = ('user', 'ativo', 'dt_inclusao')
    search_fields = ('user__nome', 'user__cpf')
    list_filter = ('ativo',)
    readonly_fields = ('dt_inclusao',)
    ordering = ('user__nome',)
    autocomplete_fields = ['user']
    actions = ['ativar_pessoas', 'desativar_pessoas']

    def ativar_pessoas(self, request, queryset):
        queryset.update(ativo=True)
        self.message_user(request, "Pessoas selecionadas foram ativadas com sucesso.")
    ativar_pessoas.short_description = 'Ativar pessoas selecionadas'

    def desativar_pessoas(self, request, queryset):
        queryset.update(ativo=False)
        self.message_user(request, "Pessoas selecionadas foram desativadas com sucesso.")
    desativar_pessoas.short_description = 'Desativar pessoas selecionadas'