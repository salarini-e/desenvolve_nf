# Generated by Django 4.2.2 on 2023-10-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_do_empreendedor', '0028_processo_digital_boleto_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='andamento_processo_digital',
            name='status',
            field=models.CharField(choices=[('nv', 'Novo'), ('ar', 'Aguardando reenvio de RG'), ('aa', 'Aguardando avaliação'), ('ap', 'Aprovado'), ('rp', 'Reprovado'), ('bg', 'Boleto gerado'), ('cn', 'Concluído')], default='n', max_length=2, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='processo_digital',
            name='status',
            field=models.CharField(choices=[('nv', 'Novo'), ('ar', 'Aguardando reenvio de RG'), ('aa', 'Aguardando avaliação'), ('ap', 'Aprovado'), ('rp', 'Reprovado'), ('bg', 'Boleto gerado'), ('cn', 'Concluído')], default='n', max_length=2, verbose_name='Status'),
        ),
    ]