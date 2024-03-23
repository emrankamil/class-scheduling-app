
from datetime import time
from django.db import models
from departments_config.models import Course
from departments_config.models import Instructor
from departments_config.models import Department

class Schedule(models.Model):

    """
    A single row in schedule table.
    """

    PROGRAM_CHOICES = [
        ('LECTURE', 'Lecture'),
        ('BREAK', 'Break'),
    ]
    DAY_CHOICES = [
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY', 'Thursday'),
        ('FRIDAY', 'Friday'),
        ('SATURDAY', 'Saturday'),
    ]

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='schedules')
    program = models.CharField(max_length=20, choices=PROGRAM_CHOICES)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    room = models.CharField(max_length=255)
    start_time = models.TimeField(default=time(0, 0))
    end_time = models.TimeField(default=time(0, 0))

    def __str__(self):
        return str(self.course)
