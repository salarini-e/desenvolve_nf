# Generated by Django 4.1.7 on 2023-02-28 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0005_palestra'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='tipo',
            field=models.CharField(choices=[('C', 'Curso'), ('P', 'Palestra')], default='C', max_length=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Palestra',
        ),
    ]
