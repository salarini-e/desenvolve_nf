# Generated by Django 3.2.15 on 2023-06-23 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamados_dev', '0005_devordemdeservico_secretaria_solicitante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devordemdeservico',
            name='motivo_reclamacao',
            field=models.TextField(verbose_name='Motivo da solicitação'),
        ),
    ]
