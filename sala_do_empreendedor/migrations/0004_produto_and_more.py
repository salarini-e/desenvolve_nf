# Generated by Django 4.2.2 on 2023-08-16 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sala_do_empreendedor', '0003_empresa_fornecedor_empresa_vitrine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, verbose_name='Nome do produto')),
                ('descricao', models.TextField(verbose_name='Descrição do produto')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('imagem', models.ImageField(upload_to='produtos/', verbose_name='Imagem do produto')),
                ('dt_register', models.DateField(auto_now_add=True, verbose_name='Data de cadastro')),
            ],
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='fornecedor',
            new_name='cadastrada_como_fornecedor',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='vitrine',
            new_name='cadastrada_na_vitrine',
        ),
        migrations.CreateModel(
            name='Registro_no_vitrine_virtual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_register', models.DateField(auto_now_add=True, verbose_name='Data de cadastro')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sala_do_empreendedor.empresa', verbose_name='Empresa')),
                ('produtos', models.ManyToManyField(to='sala_do_empreendedor.produto', verbose_name='Produtos')),
                ('user_register', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário que cadastrou')),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sala_do_empreendedor.empresa', verbose_name='Empresa'),
        ),
        migrations.AddField(
            model_name='produto',
            name='user_register',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário que cadastrou'),
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_register', models.DateField(auto_now_add=True, verbose_name='Data de cadastro')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sala_do_empreendedor.empresa', verbose_name='Empresa')),
                ('user_register', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário que cadastrou')),
            ],
        ),
    ]