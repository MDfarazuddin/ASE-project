# Generated by Django 2.1.2 on 2018-11-11 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0004_auto_20181111_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='slug',
            field=models.SlugField(max_length=20),
        ),
    ]
