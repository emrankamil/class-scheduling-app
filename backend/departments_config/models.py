from datetime import time
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Course(models.Model):
    name=models.CharField(max_length=255)
    credit_hour = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Instructor(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course, related_name='departments')
    instructors = models.ManyToManyField(Instructor, related_name='departments')
    assigned_days = ArrayField(models.CharField(max_length=15), default=list)
    rooms=ArrayField(models.CharField(max_length=255), default=list)

    morning_start_time = models.TimeField(default=time(0, 0))
    morning_end_time = models.TimeField(default=time(0, 0))
    afternoon_start_time = models.TimeField(default=time(0, 0))
    afternoon_end_time = models.TimeField(default=time(0, 0))

    def __str__(self):
        return self.name

