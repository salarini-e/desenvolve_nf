# Generated by Django 4.2.2 on 2023-09-27 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_do_empreendedor', '0022_processo_digital_licenca_sanitaria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='processo_digital',
            name='status',
            field=models.CharField(choices=[('n', 'Novo'), ('p', 'Processando'), ('a', 'Aprovado'), ('r', 'Reprovado')], default='n', max_length=1, verbose_name='Status'),
        ),
    ]