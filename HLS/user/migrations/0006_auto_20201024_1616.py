# Generated by Django 3.1.2 on 2020-10-24 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20201024_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='study_day',
        ),
        migrations.RemoveField(
            model_name='user',
            name='study_hour',
        ),
        migrations.RemoveField(
            model_name='user',
            name='study_min',
        ),
        migrations.RemoveField(
            model_name='user',
            name='study_sec',
        ),
    ]
