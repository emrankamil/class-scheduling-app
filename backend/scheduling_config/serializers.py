from rest_framework import serializers
from . import models

class SchedulingCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SchedulingCourse
        fields = '__all__'

class SchedulingDataSerializer(serializers.ModelSerializer):
    scheduling_courses = SchedulingCourseSerializer(many=True,read_only=True,)
    class Meta:
        model = models.SchedulingData
        fields = '__all__'