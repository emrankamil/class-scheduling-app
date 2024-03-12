from rest_framework import serializers
from . import models

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = [
            'name',
            'courses',
            'instructors',
            'assigned_days',
            'rooms',
            'morning_start_time',
            'morning_end_time', 
            'afternoon_start_time',
            'afternoon_end_time',
        ]
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = [
            'id',
            'name',
            'credit_hour'
        ]
class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instructor
        fields = [
            'id',
            'name',
        ]

# class ScheduleUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Department

#         def update(self, instance, validated_data):
#             return super().update(instance, validated_data) 
