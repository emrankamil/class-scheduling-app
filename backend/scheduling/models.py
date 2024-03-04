from django.db import models
from django.contrib.postgres.fields import ArrayField

class Course(models.Model):
    name=models.CharField(max_length=255)
    credit_hour = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Instructor(models.Model):
    name=models.CharField(max_length=255)
    courses = models.ManyToManyField(Course, related_name='instructors')

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course, related_name='departments')
    instructors = models.ManyToManyField(Instructor, related_name='departments')
    assigned_days = ArrayField(models.CharField(max_length=10), blank=True)

    # Time fields
    morning_start_time = models.TimeField(default=datetime.now)
    morning_end_time = models.TimeField(default=datetime.now)
    afternoon_start_time = models.TimeField(default=datetime.now)
    afternoon_end_time = models.TimeField(default=datetime.now)

    def __str__(self):
        return self.name
