# Generated by Django 3.2.15 on 2024-02-09 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_do_empreendedor', '0035_auto_20240209_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credito_facil',
            name='cnpj',
            field=models.CharField(max_length=18, null=True, verbose_name='CNPJ da empresa'),
        ),
        migrations.AlterField(
            model_name='novas_oportunidades',
            name='cpf',
            field=models.CharField(max_length=14, null=True, verbose_name='CPF'),
        ),
    ]