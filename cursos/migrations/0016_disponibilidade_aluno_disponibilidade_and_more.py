# Generated by Django 4.2.2 on 2023-10-31 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0015_alter_matricula_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disponibilidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disponibilidade', models.CharField(max_length=100, verbose_name='Disponibilidade')),
            ],
            options={
                'verbose_name': 'Disponibilidade de turno',
                'verbose_name_plural': 'Disponibilidade de turnos',
                'ordering': ['disponibilidade'],
            },
        ),
        migrations.AddField(
            model_name='aluno',
            name='disponibilidade',
            field=models.ManyToManyField(to='cursos.disponibilidade', verbose_name='Disponibilidade de turno'),
        ),
        migrations.AddField(
            model_name='turma',
            name='disponibilidade',
            field=models.ManyToManyField(to='cursos.disponibilidade', verbose_name='Disponibilidade de turno'),
        ),
    ]
