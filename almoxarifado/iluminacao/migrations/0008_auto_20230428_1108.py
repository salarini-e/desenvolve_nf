# Generated by Django 3.2.15 on 2023-04-28 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iluminacao', '0007_rename_contribuinte_ordemdeservico_cadastrado_por'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordemdeservico',
            name='nome_do_contribuinte',
            field=models.CharField(blank=True, max_length=200, verbose_name='Nome do contribuinte'),
        ),
        migrations.AddField(
            model_name='ordemdeservico',
            name='telefone_do_contribuinte',
            field=models.CharField(blank=True, max_length=12, verbose_name='Telefone do contribuinte'),
        ),
    ]
