# Generated by Django 3.1.2 on 2020-10-16 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timer',
            name='study_day',
            field=models.IntegerField(default=0, verbose_name='공부한 날'),
            preserve_default=False,
        ),
    ]
