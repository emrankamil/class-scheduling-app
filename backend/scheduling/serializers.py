from collections import defaultdict
from rest_framework import serializers
from django.db.models import Q
from .models import Schedule
from rest_framework.exceptions import ValidationError

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            'department',
            'program',
            'course',
            'instructor',
            'day',
            'room',
            'start_time',
            'end_time',
        ]

    def create(self, validated_data):
        program = validated_data.get('program')
        day = validated_data.get('day')
        instructor = validated_data.get('instructor')
        room = validated_data.get('room')
        schedule_start_time = validated_data.get('start_time')
        schedule_end_time = validated_data.get('end_time')

        # filter those rows with time which have time conflict with the new schedule
        filtered_schedules = Schedule.objects.filter(
            Q(day=day, start_time__range=(schedule_start_time, schedule_end_time)) |
            Q(day=day, end_time__range=(schedule_start_time, schedule_end_time)) |
            Q(day=day, start_time__lt=schedule_start_time, end_time__gt=schedule_end_time)
        )

        errors = defaultdict(str)
        if program == 'BREAK' and filtered_schedules.exists():
            for i , schedule in enumerate(filtered_schedules):
                errors[f'delete-{i+1}'] = f"program: {schedule.program}, day: {schedule.day}, course: {schedule.course}, instructor: {schedule.instructor}, room: {schedule.room}, time: {schedule.start_time}:{schedule.end_time}"
            
            raise ValidationError({"error": "Schedule conflicts with existing ones", "affected_programs": list(errors.values())}, code=409)
        
        for schedule in filtered_schedules:
            if schedule.room == room:
                raise serializers.ValidationError("Schedule overlaps with an existing one (the room is not availabe).")
            if schedule.instructor == instructor:
                raise serializers.ValidationError("Schedule overlaps with an existing one (the instructor is not availabe).")


        return Schedule.objects.create(**validated_data)



        ## filter the schedule data based on instructor
        # filter_schedules_instructor = Schedule.objects.filter(day=day, instructor=instructor) 

        # # filter the schedule data based on room
        # filter_schedules_room = Schedule.objects.filter(day=day, room=room) 

        # for schedule in filter_schedules_instructor:
        #     if start_time < schedule.end_time and end_time > schedule.start_time:
        #         raise serializers.ValidationError("Schedule overlaps with an existing one (the instructor is not availabe).")
        
        # for schedule in filter_schedules_room:
        #     if start_time < schedule.end_time and end_time > schedule.start_time:
        #         raise serializers.ValidationError("Schedule overlaps with an existing one (the room is not availabe).")


