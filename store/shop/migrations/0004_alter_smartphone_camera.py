# Generated by Django 3.2.3 on 2021-05-27 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210527_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='camera',
            field=models.CharField(max_length=255, verbose_name='Камера'),
        ),
    ]