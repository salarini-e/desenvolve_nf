# Generated by Django 3.2.15 on 2023-04-11 16:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('iluminacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemdeservico',
            name='numero',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Protocolo'),
        ),
    ]
