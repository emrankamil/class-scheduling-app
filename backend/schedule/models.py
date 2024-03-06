from django.db import models
from django.contrib.postgres.fields import ArrayField

class Course(models.Model):
    name=models.CharField(max_length=255)
    credit_hour = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Instructor(models.Model):
    name=models.CharField(max_length=255)
    courses = models.ManyToManyField(Course, blank=True, related_name='instructors')

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course,  blank=True, related_name='departments')
    instructors = models.ManyToManyField(Instructor, blank=True, related_name='departments')
    assigned_days = ArrayField(models.CharField(max_length=15), blank=True, default=list)

    morning_start_time = models.TimeField(auto_now_add=True)
    morning_end_time = models.TimeField(auto_now_add=True)
    afternoon_start_time = models.TimeField(auto_now_add=True)
    afternoon_end_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name
