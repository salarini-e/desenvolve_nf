# Generated by Django 3.2.15 on 2024-01-26 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_do_empreendedor', '0028_contrato_de_servico_nota_fiscal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato_de_servico',
            name='nota_fiscal',
            field=models.FileField(null=True, upload_to='contratos_pdde/nota_fiscal/', verbose_name='Nota fiscal'),
        ),
    ]
