# Generated by Django 3.2.15 on 2023-12-12 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sala_do_empreendedor', '0013_contrato_de_servico_hash'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposta_item',
            name='empresa',
        ),
        migrations.AddField(
            model_name='proposta',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sala_do_empreendedor.empresa', verbose_name='Empresa'),
            preserve_default=False,
        ),
    ]
