# Generated by Django 2.1.3 on 2018-11-12 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('S_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('S_name', models.CharField(max_length=250)),
                ('S_grade', models.CharField(blank=True, max_length=3)),
            ],
        ),
    ]
