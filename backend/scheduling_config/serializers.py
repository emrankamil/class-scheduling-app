from collections import defaultdict
import datetime
from rest_framework import serializers
from . import models
from departments_config.models import Department

class SchedulingCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SchedulingCourse
        fields = '__all__'

class SchedulingDataSerializer(serializers.ModelSerializer):
    scheduling_courses = SchedulingCourseSerializer(many=True,read_only=True,)
    possible_durations = serializers.SerializerMethodField()

    class Meta:
        model = models.SchedulingData
        fields = ['id', 'department', 'year', 'batch', 'number_of_sections', 'rooms', 'scheduling_courses', 'possible_durations']
    
    def get_possible_durations(self, obj):
        courses_data = models.SchedulingCourse.objects.all()
        deparment_data = Department.objects.get(id=obj.department.id)

        morning_start_time = deparment_data.morning_start_time
        print(type(morning_start_time))
        morning_end_time = deparment_data.morning_end_time
        afternoon_start_time = deparment_data.afternoon_start_time
        afternoon_end_time = deparment_data.afternoon_end_time

        morning_duration_minutes = (morning_end_time.hour * 60 + morning_end_time.minute) - (morning_start_time.hour * 60 + morning_start_time.minute)
        afternoon_duration_minutes = (afternoon_end_time.hour * 60 + afternoon_end_time.minute) - (afternoon_start_time.hour * 60 + afternoon_start_time.minute)

        scheduling_courses = courses_data.filter(scheduling_data=obj)

        distinct_time_durations = set()
        for course in scheduling_courses:
            for duration in course.time_durations:
                distinct_time_durations.add(duration)
        
        # return list(distinct_time_durations)

        start_times = defaultdict(set)

        for duration in distinct_time_durations:
            for i in range(morning_duration_minutes//int(duration)):
                timechange = datetime.timedelta(minutes=i*int(duration))
                start_times[duration].add(morning_start_time + timechange)
            for i in range(afternoon_duration_minutes//int(duration)):
                start_times[duration].add(afternoon_start_time + datetime.timedelta(minutes=i*int(duration)))

        return start_times