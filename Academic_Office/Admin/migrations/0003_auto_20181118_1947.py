# Generated by Django 2.1.3 on 2018-11-18 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_auto_20181118_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admins',
            name='A_id',
            field=models.CharField(max_length=3),
        ),
    ]