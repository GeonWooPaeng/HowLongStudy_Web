# Generated by Django 3.1.2 on 2020-10-24 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20201024_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='study_day',
            field=models.IntegerField(default=5, verbose_name='공부한 날'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='study_hour',
            field=models.IntegerField(default=4, verbose_name='시간'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='study_min',
            field=models.IntegerField(default=3, verbose_name='분'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='study_sec',
            field=models.IntegerField(default=6, verbose_name='초'),
            preserve_default=False,
        ),
    ]
