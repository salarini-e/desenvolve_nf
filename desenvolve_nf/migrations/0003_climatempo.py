# Generated by Django 3.2.15 on 2023-04-11 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolve_nf', '0002_carousel_index_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClimaTempo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxTemp', models.CharField(max_length=3, verbose_name='Temperatura máxima')),
                ('minTemp', models.CharField(max_length=3, verbose_name='Temperatura mínima')),
                ('madrugada', models.CharField(max_length=50, verbose_name='Clima na madrugada')),
                ('manha', models.CharField(max_length=50, verbose_name='Clima na manhã')),
                ('tarde', models.CharField(max_length=50, verbose_name='Clima na tarde')),
                ('noite', models.CharField(max_length=50, verbose_name='Clima na noite')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, unique=True)),
            ],
            options={
                'verbose_name': 'Relatório',
                'verbose_name_plural': 'Relatórios de clima',
                'ordering': ['-dt_inclusao'],
            },
        ),
    ]