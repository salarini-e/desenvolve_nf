# Generated by Django 4.2.2 on 2023-09-18 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_do_empreendedor', '0015_remove_faccao_legal_trabalha_com_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faccao_legal',
            name='outro_produto',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Protudz outro produto? Caso sim, descreva:'),
        ),
        migrations.AlterField(
            model_name='faccao_legal',
            name='situacao_remuneracao',
            field=models.CharField(choices=[('bx', 'Baixo'), ('rg', 'Regular'), ('bo', 'Bom'), ('ot', 'Ótimo')], max_length=2, verbose_name='Como você considera o valor que está sendo pago pela confecção de suas peças?'),
        ),
        migrations.AlterField(
            model_name='faccao_legal',
            name='trabalha_com',
            field=models.ManyToManyField(null=True, to='sala_do_empreendedor.trabalho_faccao', verbose_name='Trabalha com:'),
        ),
    ]