# Generated by Django 3.2.15 on 2024-07-01 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaRecadastramento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(blank=True, max_length=14, null=True, unique=True)),
                ('responsavel_tributario', models.CharField(max_length=150)),
                ('cnpj', models.CharField(blank=True, max_length=14, null=True)),
                ('nome_do_contribuinte', models.CharField(max_length=150)),
                ('celular', models.CharField(blank=True, max_length=15)),
                ('cep', models.CharField(blank=True, max_length=9)),
                ('rua', models.CharField(blank=True, max_length=150)),
                ('numero', models.CharField(blank=True, max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=50, null=True)),
                ('bairro', models.CharField(blank=True, max_length=50)),
                ('cidade', models.CharField(blank=True, max_length=50)),
                ('estado', models.CharField(blank=True, max_length=2)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requerente', models.CharField(max_length=150)),
                ('requerimento', models.CharField(max_length=20)),
                ('ano', models.IntegerField()),
                ('localizacao', models.CharField(max_length=100)),
                ('pessoa_recadastramento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financas_recadastramento.pessoarecadastramento')),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20)),
                ('pessoa_recadastramento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financas_recadastramento.pessoarecadastramento')),
            ],
        ),
    ]