# Generated by Django 3.2.15 on 2023-04-29 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iluminacao', '0008_auto_20230428_1108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordemdeservico',
            options={'ordering': ['-dt_solicitacao']},
        ),
    ]