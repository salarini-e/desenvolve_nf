# Generated by Django 3.2.15 on 2024-07-08 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos_profissionais', '0002_alter_curso_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='destaque',
            field=models.BooleanField(default=False),
        ),
    ]
