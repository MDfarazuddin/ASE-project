# Generated by Django 2.1.3 on 2018-11-18 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0007_auto_20181118_0148'),
        ('Teacher', '0005_auto_20181118_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachers',
            name='T_course',
        ),
        migrations.AddField(
            model_name='teachers',
            name='T_course_id',
            field=models.ForeignKey(default='Algorithms', on_delete=django.db.models.deletion.CASCADE, to='Student.Courses'),
            preserve_default=False,
        ),
    ]
