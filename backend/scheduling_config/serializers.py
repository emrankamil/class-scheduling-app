from collections import defaultdict
import datetime
from rest_framework import serializers

from departments_config.serializers import RoomSerializer, ReservedRoomSerializer
from . import models
from departments_config.models import Department, ReservedRoom

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Section
        fields = '__all__'

class SchedulingInstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SchedulingInstructor
        fields = '__all__'

class SchedulingCourseSerializer(serializers.ModelSerializer):
    scheduling_instructors = SchedulingInstructorSerializer(many=True,read_only=True,)
    class Meta:
        model = models.SchedulingCourse
        fields = '__all__'


class SchedulingDataSerializer(serializers.ModelSerializer):
    scheduling_courses = SchedulingCourseSerializer(many=True,read_only=True,)
    sections = serializers.SerializerMethodField()
    department_rooms = serializers.SerializerMethodField()
    reserved_rooms = serializers.SerializerMethodField()
    possible_durations = serializers.SerializerMethodField()

    class Meta:
        model = models.SchedulingData
        fields = ['id', 'department', 'year', 'batch', 'number_of_sections', 'sections', 'department_rooms','reserved_rooms', 'scheduling_courses', 'possible_durations']
    
    def get_possible_durations(self, obj):
        courses_data = models.SchedulingCourse.objects.all()
        deparment_data = Department.objects.get(id=obj.department.id)

        morning_start_time = deparment_data.morning_start_time
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

        start_times = defaultdict(set)

        for duration in distinct_time_durations:
            for i in range(morning_duration_minutes//int(duration)):
                timechange = datetime.timedelta(minutes=i*int(duration))
                time = (datetime.datetime.combine(datetime.date(1,1,1),morning_start_time) + timechange).time()
                start_times[duration].add(time)
            for i in range(afternoon_duration_minutes//int(duration)):
                timechange = datetime.timedelta(minutes=i*int(duration))
                time = (datetime.datetime.combine(datetime.date(1,1,1),afternoon_start_time) + timechange).time()
                start_times[duration].add(time)
                
        return start_times

    def get_department_rooms(self, obj):
        department_rooms = obj.rooms.filter(department=obj.department)
        return RoomSerializer(department_rooms, many=True).data

    def get_reserved_rooms(self, obj):
        reserved_rooms = obj.rooms.filter(reservations__reserved_for=obj.department)
        return RoomSerializer(reserved_rooms, many=True).data

    def get_sections(self, obj):
        sections = models.Section.objects.filter(scheduling_data=obj)
        return SectionSerializer(sections, many=True).data[:obj.number_of_sections]