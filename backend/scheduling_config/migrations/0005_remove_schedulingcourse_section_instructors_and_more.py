# Generated by Django 5.0.3 on 2024-04-14 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling_config', '0004_remove_schedulinginstructor_section_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedulingcourse',
            name='section_instructors',
        ),
        migrations.RemoveField(
            model_name='schedulinginstructor',
            name='scheduling_data',
        ),
        migrations.AddField(
            model_name='schedulinginstructor',
            name='scheduling_course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='scheduling_instructors', to='scheduling_config.schedulingcourse'),
            preserve_default=False,
        ),
    ]
