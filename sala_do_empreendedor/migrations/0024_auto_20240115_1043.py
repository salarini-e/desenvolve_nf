# Generated by Django 3.2.15 on 2024-01-15 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_do_empreendedor', '0023_auto_20240112_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='requerimentoissqn',
            name='boleto',
            field=models.FileField(blank=True, null=True, upload_to='processos/boleto/', verbose_name='Boleto'),
        ),
        migrations.AlterField(
            model_name='documentospedido',
            name='alvara_localizacao_status',
            field=models.CharField(choices=[('0', 'Aguardando avaliação'), ('1', 'Aprovado'), ('2', 'Reprovado'), ('3', 'Atualização requerida')], default='0', max_length=1, verbose_name='Status do alvará de localização e funcionamento'),
        ),
        migrations.AlterField(
            model_name='documentospedido',
            name='balancete_analitico_status',
            field=models.CharField(choices=[('0', 'Aguardando avaliação'), ('1', 'Aprovado'), ('2', 'Reprovado'), ('3', 'Atualização requerida')], default='0', max_length=1, verbose_name='Status do balancete analítico'),
        ),
        migrations.AlterField(
            model_name='documentospedido',
            name='balanco_patrimonial_status',
            field=models.CharField(choices=[('0', 'Aguardando avaliação'), ('1', 'Aprovado'), ('2', 'Reprovado'), ('3', 'Atualização requerida')], default='0', max_length=1, verbose_name='Status do balanço patrimonial'),
        ),
        migrations.AlterField(
            model_name='documentospedido',
            name='carteira_orgao_classe_status',
            field=models.CharField(choices=[('0', 'Aguardando avaliação'), ('1', 'Aprovado'), ('2', 'Reprovado'), ('3', 'Atualização requerida')], default='0', max_length=1, verbose_name='Status da carteira do órgão de classe'),
        ),
        migrations.AlterField(
            model_name='documentospedido',
            name='cnpj_copia_status',
            field=models.CharField(choices=[('0', 'Aguardando avaliação'), ('1', 'Aprovado'), ('2', 'Reprovado'), ('3', 'Atualização requerida')], default='0', max_length=1, verbose_name='Status da cópia do CNPJ'),
        ),
        migrations.AlterField(
            model_name='documentospedido',
            name='contrato_social_status',
            field=models.CharField(choices=[('0', 'Aguardando avaliação'), ('1', 'Aprovado'), ('2', 'Reprovado'), ('3', 'Atualização requerida')], default='0', max_length=1, verbose_name='Status do contrato social'),
        ),
        migrations.AlterField(
            model_name='documentospedido',
            name='dre_status',
            field=models.CharField(choices=[('0', 'Aguardando avaliação'), ('1', 'Aprovado'), ('2', 'Reprovado'), ('3', 'Atualização requerida')], default='0', max_length=1, verbose_name='Status do DRE'),
        ),
        migrations.AlterField(
            model_name='documentospedido',
            name='informacoes_cadastrais_dos_empregados_status',
            field=models.CharField(choices=[('0', 'Aguardando avaliação'), ('1', 'Aprovado'), ('2', 'Reprovado'), ('3', 'Atualização requerida')], default='0', max_length=1, verbose_name='Status das informações cadastrais dos empregados'),
        ),
        migrations.AlterField(
            model_name='documentospedido',
            name='ir_empresa_status',
            field=models.CharField(choices=[('0', 'Aguardando avaliação'), ('1', 'Aprovado'), ('2', 'Reprovado'), ('3', 'Atualização requerida')], default='0', max_length=1, verbose_name='Status do IR da empresa'),
        ),
        migrations.AlterField(
            model_name='documentospedido',
            name='profissionais_habilitados_status',
            field=models.CharField(choices=[('0', 'Aguardando avaliação'), ('1', 'Aprovado'), ('2', 'Reprovado'), ('3', 'Atualização requerida')], default='0', max_length=1, verbose_name='Status da relação dos profissionais habilitados'),
        ),
        migrations.AlterField(
            model_name='documentospedido',
            name='simples_nacional_status',
            field=models.CharField(choices=[('0', 'Aguardando avaliação'), ('1', 'Aprovado'), ('2', 'Reprovado'), ('3', 'Atualização requerida')], default='0', max_length=1, verbose_name='Status do simples nacional'),
        ),
    ]
