# Generated by Django 3.1.7 on 2021-09-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_bank', '0002_auto_20210928_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='filetypes',
            name='code',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
