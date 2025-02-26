# Generated by Django 4.2.2 on 2023-08-17 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estagio', '0026_estudante_vaga_tce'),
    ]

    operations = [
        migrations.AddField(
            model_name='locais_de_estagio',
            name='bairro',
            field=models.CharField(default='', max_length=100, verbose_name='Bairro'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='locais_de_estagio',
            name='cursos',
            field=models.ManyToManyField(to='estagio.curso'),
        ),
        migrations.AddField(
            model_name='locais_de_estagio',
            name='telefone_local',
            field=models.CharField(max_length=15, null=True, verbose_name='Telefone do local'),
        ),
        migrations.AddField(
            model_name='locais_de_estagio',
            name='telefone_responsavel',
            field=models.CharField(max_length=15, null=True, verbose_name='Telefone do responsável do local'),
        ),
        migrations.AddField(
            model_name='secretaria',
            name='telefone',
            field=models.CharField(max_length=15, null=True, verbose_name='Telefone da secretaria'),
        ),
        migrations.AddField(
            model_name='universidade',
            name='contato',
            field=models.CharField(default='', max_length=50, verbose_name='Contato do responsável de estágio da instituição'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='universidade',
            name='dt_inicio_do_termo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='universidade',
            name='logo',
            field=models.ImageField(null=True, upload_to='estagio/media/logo_universidade/'),
        ),
        migrations.AddField(
            model_name='universidade',
            name='nome_responsavel',
            field=models.CharField(default='', max_length=150, verbose_name='Nome do responsável de estágio da instituição'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='curso',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Nome do curso'),
        ),
        migrations.AlterField(
            model_name='locais_de_estagio',
            name='local',
            field=models.CharField(max_length=100, verbose_name='Nome do local'),
        ),
        migrations.AlterField(
            model_name='responsavel_universidade',
            name='cargo',
            field=models.CharField(default='Cargo do Responsável', max_length=20),
        ),
        migrations.AlterField(
            model_name='secretaria',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome da secretaria'),
        ),
        migrations.AlterField(
            model_name='universidade',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome da instituição'),
        ),
    ]
