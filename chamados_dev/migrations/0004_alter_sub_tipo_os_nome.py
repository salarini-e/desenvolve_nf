# Generated by Django 3.2.15 on 2023-06-16 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamados_dev', '0003_auto_20230616_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_tipo_os',
            name='nome',
            field=models.CharField(blank=True, max_length=100, verbose_name='Sistema'),
        ),
    ]
