# Generated by Django 3.2.15 on 2023-11-09 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0003_alter_pessoa_possui_cnpj'),
        ('desenvolve_nf', '0006_alter_carousel_index_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitacao_newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='autenticacao.pessoa')),
            ],
        ),
    ]
