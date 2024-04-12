# Generated by Django 5.0.3 on 2024-04-12 12:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0002_scheduleentry_delete_schedule'),
        ('scheduling_config', '0004_remove_schedulingcourse_time_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduleentry',
            name='section',
            field=models.CharField(default='1', max_length=10),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('scheduling_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='scheduling_config.schedulingdata')),
            ],
        ),
    ]
