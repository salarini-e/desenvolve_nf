# Generated by Django 3.2.15 on 2024-01-23 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_do_empreendedor', '0025_auto_20240115_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao_de_compras',
            name='codigo',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='solicitacao_de_compras',
            name='qnt_itens',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantidade de itens solicitados'),
        ),
    ]