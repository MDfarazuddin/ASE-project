# Generated by Django 2.1.3 on 2018-11-17 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0002_auto_20181116_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='T_email',
            field=models.EmailField(max_length=254),
        ),
    ]
