# Generated by Django 3.1.7 on 2021-10-23 22:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('a_bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_ciiv', models.CharField(max_length=100, unique=True)),
                ('macro', models.CharField(blank=True, max_length=80)),
                ('activity', models.CharField(blank=True, max_length=100)),
                ('DP1', models.CharField(blank=True, max_length=250)),
                ('DP2', models.CharField(blank=True, max_length=250)),
                ('DP3', models.CharField(blank=True, max_length=250)),
                ('R1', models.CharField(blank=True, max_length=250)),
                ('R2', models.CharField(blank=True, max_length=250)),
                ('R3', models.CharField(blank=True, max_length=250)),
                ('create_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '5- Activity',
            },
        ),
        migrations.CreateModel(
            name='OperationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('code', models.CharField(blank=True, max_length=20)),
                ('create_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '9.2- Operation Type',
            },
        ),
        migrations.CreateModel(
            name='PersonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('create_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '9.3- Person Type',
            },
        ),
        migrations.CreateModel(
            name='PrecendentCrime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('create_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '7- Crime',
            },
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('create_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '6- Risk',
            },
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('code', models.CharField(blank=True, max_length=20)),
                ('create_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '9.1- Service Type',
            },
        ),
        migrations.CreateModel(
            name='ReportBySuspicious',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(blank=True, max_length=100)),
                ('lastname', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('avg_o_act_avg', models.BooleanField(default=False)),
                ('total_o_act_avg', models.BooleanField(default=False)),
                ('transactions', models.IntegerField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('create_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('activity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suspicous_activity_type_batch', to='a_report.activity')),
                ('batch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_suspicous_activity_batch', to='a_bank.batch')),
            ],
            options={
                'verbose_name': '8.4- Report By Suspicous',
            },
        ),
        migrations.CreateModel(
            name='ReportByService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase', models.CharField(blank=True, max_length=100)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('create_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('batch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_sercvice_type_batch', to='a_bank.batch')),
                ('service_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_type_batch', to='a_report.servicetype')),
            ],
            options={
                'verbose_name': '8.3- Report By Service',
            },
        ),
        migrations.CreateModel(
            name='ReportByPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk', models.CharField(max_length=100)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('create_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('batch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_person_type_batch', to='a_bank.batch')),
                ('person_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_type_batch', to='a_report.persontype')),
            ],
            options={
                'verbose_name': '8.2- Report by Person Type',
            },
        ),
        migrations.CreateModel(
            name='ReportByOperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(blank=True, null=True)),
                ('create_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('batch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_operation_type_batch', to='a_bank.batch')),
                ('operation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operatioon_type_batch', to='a_report.operationtype')),
            ],
            options={
                'verbose_name': '8.1- Report By Operations',
            },
        ),
        migrations.CreateModel(
            name='ReportByActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(blank=True, null=True)),
                ('create_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('batch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_activity_type_batch', to='a_bank.batch')),
                ('precendent_crime_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='precedent_crime_risk_type_batch', to='a_report.precendentcrime')),
                ('risk_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='risk_batch', to='a_report.risk')),
            ],
            options={
                'verbose_name': '8.0- Report Precedent Crime and Risk',
            },
        ),
        migrations.AddField(
            model_name='activity',
            name='precedent_crime_ids',
            field=models.ManyToManyField(blank=True, to='a_report.PrecendentCrime'),
        ),
        migrations.AddField(
            model_name='activity',
            name='risk_ids',
            field=models.ManyToManyField(blank=True, to='a_report.Risk'),
        ),
    ]