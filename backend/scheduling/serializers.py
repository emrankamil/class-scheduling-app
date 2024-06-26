from requests import Response
from rest_framework import serializers
from django.db.models import Q
from .models import ScheduleEntry

class ScheduleEntrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ScheduleEntry
        fields = 'parent_schedule', 'course','section', 'instructor', 'day', 'room', 'start_time', 'end_time'

    def validate(self, attrs):
        parent_schedule = attrs.get('parent_schedule')
        section = attrs.get('section')
        course = attrs.get('course')
        instructor = attrs.get('instructor')
        room = attrs.get('room')
        day = attrs.get('day')
        schedule_start_time = attrs.get('start_time')
        schedule_end_time = attrs.get('end_time')

        # if parent_schedule:
        #     if not parent_schedule.scheduling_courses.filter(course=course).exists():
        #         raise serializers.ValidationError("Course must belong to the parent_schedule's scheduling courses.")
        #     if not course.scheduling_courses.filter(instructors=instructor).exists():
        #         raise serializers.ValidationError("Instructor must belong to the respective course.")
        #     if not parent_schedule.rooms.filter(pk=room.pk).exists():
        #         raise serializers.ValidationError("Room must belong to the parent_schedule's rooms.")

        filtered_schedules = ScheduleEntry.objects.filter(
            Q(day=day, start_time__lte=schedule_start_time, end_time__gt=schedule_start_time) | #start_time__range=(schedule_start_time, schedule_end_time)
            Q(day=day, start_time__lt=schedule_end_time, end_time__gte=schedule_end_time) |
            Q(day=day, start_time__gt=schedule_start_time, end_time__lt=schedule_end_time)
        )

        if filtered_schedules.exists():
            for schedule in filtered_schedules:
                if schedule.section == section:
                    raise serializers.ValidationError("Schedule overlaps with an existing one (the time is not availabe).")
                if schedule.room == room:
                    raise serializers.ValidationError(f"Schedule overlaps with an existing one (the room {room} is not availabe).")
                if schedule.instructor == instructor:
                    raise serializers.ValidationError("Schedule overlaps with an existing one (the instructor is not availabe).")
    
        return attrs