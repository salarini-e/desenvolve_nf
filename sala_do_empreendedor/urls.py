from django.urls import path
from . import views
 
app_name='empreendedor'
urlpatterns = [
    path('', views.index, name='index'),
    
    path('consultar-protocolo', views.consultar_protocolo, name='consultar_protocolo'),
    
    path('conheca-nossa-sala', views.conheca_nossa_sala, name='conheca_nossa_sala'),
    
    path('minha-empresa', views.minha_empresa, name='minha_empresa'),
    path('minha-empresa/cadastrar', views.cadastrar_empresa, name='cadastrar_empresa'),
    path('minha-empresa/<id>/editar/', views.editar_empresa, name='editar_empresa'),
    path('minha-empresa/<id>/vitrine/', views.minha_vitrine, name='minha_vitrine'),
    path('minha-empresa/<id>/vitrine/alterar-logo', views.enviar_ou_trocar_logo, name='enviar_ou_trocar_logo'),
    path('minha-empresa/<id>/cadastrar-vitrine', views.cadastrar_vitrine, name='cadastrar_vitrine'),
    path('minha-empresa/<id>/vitrine/cadastrar-produto/', views.casdastrar_produto, name='cadastrar_produto'),
    path('faccao-legal/', views.faccao_legal, name='faccao_legal'),
    path('faccao-legal/cadastrar/', views.cadastrar_faccao_legal, name='cadastrar_faccao_legal'),
    path('vitrine-virtual', views.vitrine_virtual, name='vitrine_virtual'),
    path('cadastro-fornecedores-e-compras-publicas', views.cadastro_fornecedores_e_compras_publicas, name='compras_publicas'),
    
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
    path('ja-sou-mei/relatorioMensal', views.relatorioMensal, name="relatorioMensal"),
    path('ja-sou-mei/pagamentoDeContribuicaoMensal', views.pagamentoDeContribuicaoMensal, name="pagamentoDeContribuicaoMensal"),
    path('ja-sou-mei/solucoesFinanceiras', views.solucoesFinanceiras, name="solucoesFinanceiras"),
    path('ja-sou-mei/certidoesEComprovantes', views.certidoesEComprovantes, name="certidoesEComprovantes"),
    path('ja-sou-mei/declaracaoAnualDeFaturamento', views.declaracaoAnualDeFaturamento, name="declaracaoAnualDeFaturamento"),
    path('ja-sou-mei/dispensaDeAlvara', views.dispensaDeAlvara, name="dispensaDeAlvara"),
    
    path('abertuda-de-empresa', views.abertura_de_empresa, name='abertura_de_empresa'),
    path('iss-autonomos', views.iss_autonomos, name='iss_autonomos'),
    path('legislacao', views.legislacao, name='legislacao'),
    path('oportunidade-de-negocios', views.oportunidade_de_negocios, name='oportunidade'),
    path('admin/', views.sala_do_empreendedor_admin, name='admin'),
    path('admin/mapeamento-empresa-e-fornecedores', views.mapeamento_empresa_e_fornecedores, name='mapeamento_empresa_e_fornecedores'),
    path('faccao-legal/cadastrar/checkcnpj/', views.checkCNPJ, name='checkcnpj'),
    
    #PROCESSOS
    path('checkCPF/', views.checkCPF, name='checkCPF'),
    path('checkProfissao/', views.checkProfissao, name='checkProfissao'),
    path('muda-status-rg/', views.mudaStatusRG, name='mudaStatusRG'),
    path('muda-status-comprovante/', views.mudaStatusComprovante, name='mudaStatusComprovante'),
    path('muda-status-Ccertificado/', views.mudaStatusCertificado, name='mudaStatusCertificado'),
    path('muda-status-licenca/', views.mudaStatusLicenca, name='mudaStatusLicenca'),
    path('muda-status-espelho/', views.mudaStatusEspelho, name='mudaStatusEspelho'),
    path('adm/processos-digitais/', views.processos_digitais_admin, name='processos_digitais_admin'),
    path('adm/processos-digitais/<id>/', views.andamento_processo, name='andamento_processo_admin'),
    path('adm/processos-digitais/<id>/novo-andamento/', views.novo_andamento_processo, name='novo_andamento_processo_admin'),
    path('processos/criar-novo/requerimento-iss/', views.requerimento_iss, name='requerimento_iss'),
    path('adm/processos/criar-novo/requerimento-iss/', views.requerimento_iss_admin, name='requerimento_iss_admin'),
]