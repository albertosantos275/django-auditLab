# Generated by Django 3.1.7 on 2021-10-09 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a_bank', '0005_auto_20211009_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='file_type_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_types_bank', to='a_bank.filetypes'),
        ),
    ]
