from rest_framework import serializers
from . import models

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instructor
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    department_courses = CourseSerializer(many=True,)
    department_rooms = RoomSerializer(many=True,)
    department_instructors = InstructorSerializer(many=True,)

    class Meta:
        model = models.Department
        fields = fields = ['name', 'department_courses', 'department_rooms', 'department_instructors', 'assigned_days', 'morning_start_time', 'morning_end_time', 'afternoon_start_time', 'afternoon_end_time']
