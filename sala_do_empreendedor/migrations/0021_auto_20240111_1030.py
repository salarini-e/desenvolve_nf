# Generated by Django 3.2.15 on 2024-01-11 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sala_do_empreendedor', '0020_auto_20240109_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='requerimentoiss',
            name='dt_atualizacao',
            field=models.DateField(auto_now=True, null=True, verbose_name='Data de atualização'),
        ),
        migrations.AddField(
            model_name='requerimentoiss',
            name='dt_solicitacao',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Data de solicitação'),
        ),
        migrations.AlterField(
            model_name='requerimentoiss',
            name='processo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sala_do_empreendedor.processo_digital', verbose_name='Processo'),
        ),
    ]
