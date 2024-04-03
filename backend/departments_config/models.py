from datetime import time
from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from django.core.exceptions import ValidationError
from .validators import validate_course_data, validate_instructor_data
# def validate_course_data(value):
#     try:
#         data = value
#         if not isinstance(data, dict):
#             raise ValidationError('Invalid JSON: Must be a dictionary.')
        
#         for course_id, course_info in data.items():
#             if not isinstance(course_info, dict):
#                 raise ValidationError(f'Invalid value for course {course_id}: Must be a dictionary.')
            
#             if not Course.objects.filter(id=course_id).exists():
#                 raise ValidationError(f'Course with ID {course_id} does not exist.')
                
#             for duration, frequency in course_info.items():
#                 if not isinstance(duration, int) or not isinstance(frequency, int):
#                     raise ValidationError(f'Invalid duration or frequency for course {course_id}.')
#     except ValueError:
#         raise ValidationError('Invalid JSON format.')
    
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
    
class Department(models.Model):
    name = models.CharField(max_length=255)
    assigned_days = ArrayField(models.CharField(max_length=15), default=list)
    # courses = models.ManyToManyField('Course', related_name='department_courses')
    # instructors = models.ManyToManyField('Instructor', related_name='department_instructors')
    # rooms=ArrayField(models.CharField(max_length=255), default=list)

    morning_start_time = models.TimeField(default=time(0, 0))
    morning_end_time = models.TimeField(default=time(0, 0))
    afternoon_start_time = models.TimeField(default=time(0, 0))
    afternoon_end_time = models.TimeField(default=time(0, 0))

    def __str__(self):
        return str(self.name)

class DepartmentYear(models.Model):

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_years')
    year = models.PositiveIntegerField()
    batch = models.PositiveIntegerField()
    number_of_sections = models.PositiveIntegerField(default=1)
    courses = models.JSONField(validators=[validate_course_data]) # a list of mappings between course id and another list of mappings between time_duration and frequescy of that duration
    instructors = models.JSONField(validators=[validate_instructor_data]) # a list of mappings between instructor id and course id that instructor is teaching
    rooms= models.ManyToManyField('Room', related_name='department_year_rooms')

    def __str__(self):
        return f"{self.department.name}-{self.year}-{self.batch}"