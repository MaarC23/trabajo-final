# Generated by Django 3.0 on 2021-12-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0002_auto_20211220_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='tema_entre1y17',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]