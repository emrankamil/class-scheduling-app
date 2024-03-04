from rest_framework import serializers
from . import models

class SchedulingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = [
            'name',
            'courses',
            'instructors',
            'assigned_days',
            'morning_start_time',
            'morning_end_time', 
            'afternoon_start_time',
            'afternoon_end_time'
        ]

# class ScheduleUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Department

#         def update(self, instance, validated_data):
#             return super().update(instance, validated_data) 