# Generated by Django 3.2.15 on 2023-11-09 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0018_auto_20231107_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso_ensino_superior',
            name='url',
            field=models.URLField(default='#'),
        ),
    ]