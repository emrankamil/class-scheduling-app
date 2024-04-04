# Generated by Django 5.0.3 on 2024-04-03 12:13

import departments_config.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments_config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstructorCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments_config.course')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments_config.instructor')),
            ],
        ),
        migrations.AlterField(
            model_name='departmentyear',
            name='instructors',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_year_instructors', to='departments_config.instructorcourse'),
        ),
        migrations.CreateModel(
            name='SingleCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_durations', models.JSONField(validators=[departments_config.validators.validate_instructor_data])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments_config.course')),
            ],
        ),
        migrations.AlterField(
            model_name='departmentyear',
            name='courses',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_year_courses', to='departments_config.singlecourse'),
        ),
    ]
