from django.urls import path
from . import views
 
app_name='empreendedor'
urlpatterns = [
    path('', views.index, name='index'),
    path('consultar-protocolo', views.consultar_protocolo, name='consultar_protocolo'),
    path('faccao-legal', views.faccao_legal, name='faccao_legal'),
    path('vitrine-virtual', views.vitrine_virtual, name='vitrine_virtual'),
    
    path('quero-ser-mei', views.quero_ser_mei, name='quero_ser_mei'),
    path('quero-ser-mei/por-que-ser-mei', views.por_que_ser_mei, name='por_que_ser_mei'),
    path('quero-ser-mei/o-que-voce-precisa-saber-antes-de-se-tornar-um-mei', views.o_que_precisa_saber_para_ser_mei, name='o_que_precisa_saber_para_ser_mei'),
    path('quero-ser-mei/jornada-empreendedora', views.jornada_empreendedora, name='jornada_empreendedora'),
    path('quero-ser-mei/documentosNecessarios', views.documentosNecessarios, name='documentosNecessarios'),
    path('quero-ser-mei/quaisAsOcupacoesQuePodemSerMei', views.quaisAsOcupacoesQuePodemSerMei, name='quaisAsOcupacoesQuePodemSerMei'),
    path('quero-ser-mei/dicasDeSegurancaDaVigilanciaSanitaria', views.dicasDeSegurancaDaVigilanciaSanitaria, name='dicasDeSegurancaDaVigilanciaSanitaria'),
    path('quero-ser-mei/dicasDeSegurançaDoCorpoDeBombeiros', views.dicasDeSegurançaDoCorpoDeBombeiros, name='dicasDeSegurançaDoCorpoDeBombeiros'),
    path('quero-ser-mei/dicasDeMeioAmbiente', views.dicasDeMeioAmbiente, name='dicasDeMeioAmbiente'),
    path('quero-ser-mei/prepareSe', views.prepareSe, name='prepareSe'),
    path('quero-ser-mei/transportadorAutonomoDeCargas', views.transportadorAutonomoDeCargas, name='transportadorAutonomoDeCargas'),
    path('quero-ser-mei/direitosEObrigacoes', views.direitosEObrigacoes, name='direitosEObrigacoes'),
    path('quero-ser-mei/registrocadastur', views.registrocadastur, name="registrocadastur"),
    path('ja-sou-mei', views.ja_sou_mei, name='ja_sou_mei'),
    path('ja-sou-mei/emissaoDeComprovante', views.emissaoDeComprovante, name="emissaoDeComprovante"),
    path('ja-sou-mei/atualizacaoCadastral', views.atualizacaoCadastral, name="atualizacaoCadastral"),
    path('ja-sou-mei/capacita', views.capacita, name="capacita"),
    path('ja-sou-mei/notaFiscal', views.notaFiscal, name="notaFiscal"),
    path('abertuda-de-empresa', views.abertura_de_empresa, name='abertura_de_empresa'),

]