# Generated by Django 3.2.17 on 2023-03-07 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolve_nf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel_index',
            name='url',
            field=models.CharField(blank=True, max_length=64, verbose_name='Url, caso tenha para redirecionar'),
        ),
    ]