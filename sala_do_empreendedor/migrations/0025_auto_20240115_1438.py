# Generated by Django 3.2.15 on 2024-01-15 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_do_empreendedor', '0024_auto_20240115_1043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profissao',
            options={'ordering': ['nome']},
        ),
        migrations.AlterField(
            model_name='processo_digital',
            name='dt_atualizacao',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Data de atualização'),
        ),
        migrations.AlterField(
            model_name='processo_digital',
            name='dt_solicitacao',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de solicitação'),
        ),
    ]