# Generated by Django 4.2.2 on 2023-09-27 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sala_do_empreendedor', '0024_andamento_processo_digital_diploma_ou_certificado_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='andamento_processo_digital',
            name='comprovante_endereco_status',
        ),
        migrations.RemoveField(
            model_name='andamento_processo_digital',
            name='diploma_ou_certificado_status',
        ),
        migrations.RemoveField(
            model_name='andamento_processo_digital',
            name='espelho_iptu_status',
        ),
        migrations.RemoveField(
            model_name='andamento_processo_digital',
            name='licenca_sanitaria',
        ),
        migrations.RemoveField(
            model_name='andamento_processo_digital',
            name='rg_status',
        ),
        migrations.CreateModel(
            name='Processo_Status_Documentos_Anexos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rg_status', models.CharField(choices=[('0', 'Aguardando avaliação'), ('1', 'Aprovado'), ('2', 'Reprovado')], default='0', max_length=1, verbose_name='Status do RG')),
                ('comprovante_endereco_status', models.CharField(choices=[('0', 'Aguardando avaliação'), ('1', 'Aprovado'), ('2', 'Reprovado')], default='0', max_length=1, verbose_name='Status do comprovante de endereço')),
                ('diploma_ou_certificado_status', models.CharField(choices=[('0', 'Aguardando avaliação'), ('1', 'Aprovado'), ('2', 'Reprovado')], default='0', max_length=1, verbose_name='Status do diploma ou certificado')),
                ('licenca_sanitaria', models.CharField(choices=[('0', 'Aguardando avaliação'), ('1', 'Aprovado'), ('2', 'Reprovado')], default='0', max_length=1, verbose_name='Status da licença sanitária')),
                ('espelho_iptu_status', models.CharField(choices=[('0', 'Aguardando avaliação'), ('1', 'Aprovado'), ('2', 'Reprovado')], default='0', max_length=1, verbose_name='Status do espelho do IPTU')),
                ('processo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sala_do_empreendedor.processo_digital', verbose_name='Processo')),
            ],
        ),
    ]