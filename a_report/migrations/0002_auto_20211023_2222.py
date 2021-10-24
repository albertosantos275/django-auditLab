# Generated by Django 3.1.7 on 2021-10-23 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a_report', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'R1- Activities'},
        ),
        migrations.AlterModelOptions(
            name='operationtype',
            options={'verbose_name': 'R4- Operation Type'},
        ),
        migrations.AlterModelOptions(
            name='persontype',
            options={'verbose_name': 'R5- Person Type'},
        ),
        migrations.AlterModelOptions(
            name='precendentcrime',
            options={'verbose_name': 'R3- Crime'},
        ),
        migrations.AlterModelOptions(
            name='reportbyactivity',
            options={'verbose_name': '8.0- Report Crime and Risk'},
        ),
        migrations.AlterModelOptions(
            name='risk',
            options={'verbose_name': 'R2- Risk'},
        ),
        migrations.AlterModelOptions(
            name='servicetype',
            options={'verbose_name': 'R6- Service Type'},
        ),
        migrations.RemoveField(
            model_name='activity',
            name='DP1',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='DP2',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='DP3',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='R1',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='R2',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='R3',
        ),
        migrations.AddField(
            model_name='reportbyactivity',
            name='activity_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_type_batch', to='a_report.activity'),
        ),
    ]
