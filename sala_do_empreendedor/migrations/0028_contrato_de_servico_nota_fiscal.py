# Generated by Django 3.2.15 on 2024-01-26 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_do_empreendedor', '0027_alter_solicitacao_de_compras_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato_de_servico',
            name='nota_fiscal',
            field=models.FileField(blank=True, null=True, upload_to='contratos_pdde/nota_fiscal/', verbose_name='Nota fiscal'),
        ),
    ]
