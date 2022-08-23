# Generated by Django 3.2.15 on 2022-08-23 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cursos', '0002_curso_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='dt_alteracao',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='dt_inclusao',
            field=models.DateField(auto_now_add=True, default='2022-08-23'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curso',
            name='user_inclusao',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='userInclusao', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curso',
            name='user_ultima_alteracao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='userAlteracao', to='auth.user'),
            preserve_default=False,
        ),
    ]