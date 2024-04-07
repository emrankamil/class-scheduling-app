
from datetime import time
from django.db import models
from departments_config.models import Course
from departments_config.models import Instructor
from departments_config.models import Room
from scheduling_config.models import SchedulingData

class ScheduleEntry(models.Model):

    """
    A single row in schedule table.
    """
    DAY_CHOICES = [
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY', 'Thursday'),
        ('FRIDAY', 'Friday'),
        ('SATURDAY', 'Saturday'),
    ]

    parent_schedule = models.ForeignKey(SchedulingData, on_delete=models.CASCADE, related_name='related_schedules')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='related_schedules')
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='related_schedules')
    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='related_schedules')
    start_time = models.TimeField(default=time(0, 0))
    end_time = models.TimeField(default=time(0, 0))

    def __str__(self):
        return f'{self.course.name} - {self.day} - {self.start_time} - {self.end_time} - {self.room.name}'
