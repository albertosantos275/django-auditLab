# Generated by Django 3.1.7 on 2021-08-08 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_bank', '0003_batch_store_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='processed_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]