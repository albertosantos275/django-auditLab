# Generated by Django 3.1.7 on 2021-10-08 23:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_bank', '0004_auto_20211008_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_ciiv', models.CharField(max_length=100, unique=True)),
                ('macro', models.CharField(blank=True, max_length=80)),
                ('activity', models.CharField(blank=True, max_length=20)),
                ('DP1', models.CharField(blank=True, max_length=100)),
                ('DP2', models.CharField(blank=True, max_length=100)),
                ('DP3', models.CharField(blank=True, max_length=100)),
                ('R1', models.CharField(blank=True, max_length=100)),
                ('R2', models.CharField(blank=True, max_length=100)),
                ('R3', models.CharField(blank=True, max_length=100)),
                ('create_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '3-File Type',
            },
        ),
    ]