# Generated by Django 3.1.7 on 2021-10-09 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_bank', '0003_auto_20211009_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precendentcrime',
            name='code',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='risk',
            name='code',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
