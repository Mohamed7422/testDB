# Generated by Django 5.1.4 on 2024-12-19 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('base_hourly_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('overtime_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.client')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project')),
            ],
        ),
        migrations.CreateModel(
            name='WorkLog',
            fields=[
                ('work_log_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_worked', models.DateField()),
                ('hours_logged', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_overtime', models.BooleanField(default=False)),
                ('comments', models.TextField(blank=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.employee')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.task')),
            ],
        ),
    ]