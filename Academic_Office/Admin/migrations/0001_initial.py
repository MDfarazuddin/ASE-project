# Generated by Django 2.1.3 on 2018-11-18 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A_id', models.CharField(max_length=15)),
                ('A_name', models.CharField(max_length=20)),
                ('T_password', models.CharField(max_length=50)),
            ],
        ),
    ]
