# Generated by Django 3.2.15 on 2024-04-04 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0002_pauta_de_julgamento_dt_inclusao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ata',
            name='texto',
        ),
        migrations.AddField(
            model_name='ata',
            name='ata',
            field=models.FileField(null=True, upload_to='atas/', verbose_name='Arquivo da Ata'),
        ),
    ]