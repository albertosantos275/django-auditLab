# Generated by Django 3.1.7 on 2021-10-09 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_bank', '0008_auto_20211009_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='number_files_submitted',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
