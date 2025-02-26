# Generated by Django 3.2.15 on 2024-11-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_do_empreendedor', '0049_auto_20241112_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='diasDaSemanaNatal_Artesao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_semana', models.CharField(max_length=128, null=True, verbose_name='Dia da semana')),
                ('dt_register', models.DateField(auto_now_add=True, verbose_name='Data de cadastro')),
            ],
        ),
        migrations.AddField(
            model_name='natal_artesao',
            name='dias_que_pode_trabalhar',
            field=models.ManyToManyField(null=True, to='sala_do_empreendedor.diasDaSemanaNatal_Artesao', verbose_name='Quais dias da semana você tem disponibilidade para estar na feira?'),
        ),
    ]
