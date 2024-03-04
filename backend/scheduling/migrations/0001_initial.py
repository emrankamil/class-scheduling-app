# Generated by Django 3.2.7 on 2024-03-02 22:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('credit_hour', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('courses', models.ManyToManyField(related_name='instructors', to='scheduling.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('assigned_days', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), blank=True, size=None)),
                ('courses', models.ManyToManyField(related_name='departments', to='scheduling.Course')),
                ('instructors', models.ManyToManyField(related_name='departments', to='scheduling.Instructor')),
            ],
        ),
    ]