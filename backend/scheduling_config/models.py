from django.db import models
from django.contrib.postgres.fields import ArrayField
from .validators import validate_time_durations_data
from departments_config.models import Department, Course, Instructor, Room

class SchedulingCourse(models.Model):
    scheduling_data = models.ForeignKey('SchedulingData', on_delete=models.CASCADE, related_name='scheduling_courses', related_query_name='all_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='scheduling_courses')
    instructors = models.ManyToManyField(Instructor, related_name='scheduling_courses')
    rooms = models.ManyToManyField(Room, related_name='scheduling_courses')
    time_durations = ArrayField(models.IntegerField(), default=list)
    
    def __str__(self):
        return f"{self.course.name}-{self.scheduling_data}"

class Section(models.Model):
    name = models.CharField(max_length=100)
    scheduling_data = models.ForeignKey('SchedulingData', on_delete=models.CASCADE, related_name='sections')

    def __str__(self):
        return str(self.name)
    
class SchedulingData(models.Model):

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_years')
    year = models.PositiveIntegerField()
    batch = models.PositiveIntegerField()
    number_of_sections = models.PositiveIntegerField(default=1)
    rooms= models.ManyToManyField(Room, related_name='scheduling_rooms')

    def __str__(self):
        return f"{self.department.name}-{self.year}-{self.batch}"
    

