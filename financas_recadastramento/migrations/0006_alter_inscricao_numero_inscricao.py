# Generated by Django 3.2.15 on 2024-08-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas_recadastramento', '0005_auto_20240717_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='numero_inscricao',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
