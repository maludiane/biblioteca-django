# Generated by Django 5.1 on 2024-11-27 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_colecao_owner_alter_autor_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
