# Generated by Django 3.2.15 on 2024-02-16 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_do_empreendedor', '0040_auto_20240215_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='agente_cartorio',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email para receber notificação de processo'),
        ),
        migrations.AddField(
            model_name='agente_divida_fiscal',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email para receber notificação de processo'),
        ),
        migrations.AddField(
            model_name='agente_procuradoria',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email para receber notificação de processo'),
        ),
        migrations.AddField(
            model_name='agente_sanitario',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email para receber notificação de processo'),
        ),
        migrations.AddField(
            model_name='agente_tributario',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email para receber notificação de processo'),
        ),
    ]
