# Generated by Django 3.0 on 2021-12-23 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0005_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='titulo',
            field=models.CharField(max_length=20),
        ),
    ]
