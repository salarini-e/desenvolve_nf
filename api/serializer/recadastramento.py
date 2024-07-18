from rest_framework import serializers
from financas_recadastramento.models import PessoaRecadastramento

class PessoaRecadastramentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PessoaRecadastramento
        fields = '__all__'
