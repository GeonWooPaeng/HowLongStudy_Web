# Generated by Django 3.1.2 on 2020-10-24 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0005_auto_20201024_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timer',
            name='study_day',
        ),
        migrations.RemoveField(
            model_name='timer',
            name='study_hour',
        ),
        migrations.RemoveField(
            model_name='timer',
            name='study_min',
        ),
        migrations.RemoveField(
            model_name='timer',
            name='study_sec',
        ),
    ]
