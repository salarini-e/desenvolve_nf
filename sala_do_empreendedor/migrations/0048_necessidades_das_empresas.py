# Generated by Django 3.2.15 on 2024-05-28 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sala_do_empreendedor', '0047_auto_20240404_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Necessidades_das_Empresas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacitacao_empresarial', models.BooleanField(default=False, verbose_name='Capacitação empresarial')),
                ('capacitacao_profissional', models.BooleanField(default=False, verbose_name='Capacitação profissional')),
                ('credito', models.BooleanField(default=False, verbose_name='Crédito')),
                ('consultoria', models.BooleanField(default=False, verbose_name='Consultoria')),
                ('outro', models.BooleanField(default=False, verbose_name='Outro')),
                ('outro_descricao', models.CharField(blank=True, max_length=128, null=True, verbose_name='Qual outra necessidade?')),
                ('dt_inclusao', models.DateField(auto_now_add=True, verbose_name='Data de inclusão')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sala_do_empreendedor.empresa', verbose_name='Empresa')),
                ('user_register', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário que cadastrou')),
            ],
        ),
    ]
