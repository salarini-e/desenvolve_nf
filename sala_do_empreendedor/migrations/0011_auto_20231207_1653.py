# Generated by Django 3.2.15 on 2023-12-07 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_do_empreendedor', '0010_auto_20231207_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitacao_de_compras',
            name='ramo_atuacao',
        ),
        migrations.AddField(
            model_name='solicitacao_de_compras',
            name='ramo_atuacao',
            field=models.ManyToManyField(blank=True, null=True, to='sala_do_empreendedor.Ramo_de_Atuacao', verbose_name='Enviar mensagem para as empresas com os seguintes ramos de atuação:'),
        ),
    ]
