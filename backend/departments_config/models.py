from datetime import time
from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from .validators import validate_course_data, validate_instructor_data
    
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
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
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

# class SingleCourse(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     time_durations = models.JSONField(validators=[validate_instructor_data]) 

#     def __str__(self):
#         return f"{self.course.name}"

# class InstructorCourse(models.Model):
#     instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.instructor.name}-{self.course.name}"
    
# class DepartmentYear(models.Model):

#     department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_years')
#     year = models.PositiveIntegerField()
#     batch = models.PositiveIntegerField()
#     number_of_sections = models.PositiveIntegerField(default=1)
#     courses = models.ForeignKey(SingleCourse, on_delete=models.CASCADE, related_name='department_year_courses')# a list of mappings between course id and another list of mappings between time_duration and frequescy of that duration
#     instructors = models.ForeignKey(InstructorCourse, on_delete=models.CASCADE, related_name='department_year_instructors') # a list of mappings between instructor id and course id that instructor is teaching
#     rooms= models.ManyToManyField('Room', related_name='department_year_rooms')

#     def __str__(self):
#         return f"{self.department.name}-{self.year}-{self.batch}"
    
    