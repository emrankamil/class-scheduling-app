from django.db import models
from .validators import validate_time_durations_data
from departments_config.models import Department, Course, Instructor, Room

class SchedulingCourse(models.Model):
    scheduling_data = models.ForeignKey('SchedulingData', on_delete=models.CASCADE, related_name='scheduling_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='scheduling_courses')
    instructors = models.ManyToManyField(Instructor, related_name='scheduling_instructors')
    time_durations = models.JSONField(validators=[validate_time_durations_data]) 
    
    def __str__(self):
        return f"{self.course.name}-{self.scheduling_data}"
    
class SchedulingData(models.Model):

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_years')
    year = models.PositiveIntegerField()
    batch = models.PositiveIntegerField()
    number_of_sections = models.PositiveIntegerField(default=1)
    rooms= models.ManyToManyField(Room, related_name='scheduling_rooms')
    # instructors = models.ForeignKey(InstructorCourse, on_delete=models.CASCADE, related_name='department_year_instructors') 

    def __str__(self):
        return f"{self.department.name}-{self.year}-{self.batch}"
    
    