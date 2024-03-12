from rest_framework import serializers
from . import models

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shedule
        fields = [
            'name',
            'courses',
            'instructors',
            'assigned_days',
            'rooms',
            'available_times',
        ]