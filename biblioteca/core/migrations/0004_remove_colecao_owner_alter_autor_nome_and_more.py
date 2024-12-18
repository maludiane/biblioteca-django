# Generated by Django 5.1 on 2024-11-27 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_colecao_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colecao',
            name='owner',
        ),
        migrations.AlterField(
            model_name='autor',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livros', to='core.autor'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livros', to='core.categoria'),
        ),
    ]
