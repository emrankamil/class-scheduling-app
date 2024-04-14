from datetime import time
from django.db import models
from django.contrib.postgres.fields import ArrayField
from rest_framework.exceptions import ValidationError

class Course(models.Model):
    name = models.CharField(max_length=255)
    credit_hour = models.IntegerField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='department_courses')

    def __str__(self):
        return str(self.name)

class Instructor(models.Model):
    name=models.CharField(max_length=255)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='department_instructors')

    def __str__(self):
        return str(self.name)

class Room(models.Model):
    name=models.CharField(max_length=255)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='department_rooms')

    def __str__(self):
        return str(self.name)

class ReservedRoom(models.Model):
    DAY_CHOICES = [
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY', 'Thursday'),
        ('FRIDAY', 'Friday'),
        ('SATURDAY', 'Saturday'),
    ]
    
    reserved_for = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='reserved_rooms')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    reserved_days = models.CharField(max_length=20, choices=DAY_CHOICES)
    start_time = models.TimeField(default=time(0, 0))
    end_time = models.TimeField(default=time(0, 0))

    def __str__(self):
        return str(self.room.name)
    
class Department(models.Model):
    name = models.CharField(max_length=255)
    assigned_days = ArrayField(models.CharField(max_length=15), default=list)

    morning_start_time = models.TimeField(default=time(0, 0))
    morning_end_time = models.TimeField(default=time(0, 0))
    afternoon_start_time = models.TimeField(default=time(0, 0))
    afternoon_end_time = models.TimeField(default=time(0, 0))

    def __str__(self):
        return str(self.name)