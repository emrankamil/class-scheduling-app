from django.db import models
from django.contrib.postgres.fields import ArrayField
from departments_config.models import Course
from departments_config.models import Instructor

class Schedule(models.Model):
    name = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course,  blank=True, related_name='schedule')
    instructors = models.ManyToManyField(Instructor, blank=True, related_name='schedule')
    assigned_days = ArrayField(models.CharField(max_length=15), blank=True, default=list)
    rooms = ArrayField(models.CharField(max_length=255), blank=True, default=list)
    available_times = ArrayField(models.CharField(max_length=20), blank=True, default=list)

    def __str__(self):
        return self.name
