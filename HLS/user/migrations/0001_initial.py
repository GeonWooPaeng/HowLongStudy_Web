# Generated by Django 3.1.2 on 2020-10-07 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='이메일')),
                ('password', models.CharField(max_length=128, verbose_name='비밀번호')),
                ('level', models.CharField(max_length=8, verbose_name='등급')),
                ('register_data', models.DateField(auto_now_add=True, verbose_name='등록 날짜')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'user',
            },
        ),
    ]
