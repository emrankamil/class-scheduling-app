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

class ReservedRoomSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if data['reserved_for'] == data['room'].department:
            raise serializers.ValidationError("A room cannot be reserved for its owning department.")
        return data
    
    class Meta:
        model = models.ReservedRoom
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    reservations = ReservedRoomSerializer(many=True,read_only=True,)
    class Meta:
        model = models.Room
        fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):
    department_courses = CourseSerializer(many=True,read_only=True,)
    department_rooms = RoomSerializer(many=True,read_only=True,)
    department_instructors = InstructorSerializer(many=True,read_only=True,)

    class Meta:
        model = models.Department
        fields = fields = ['name', 'department_courses', 'department_rooms', 'department_instructors', 'assigned_days','reserved_rooms', 'morning_start_time', 'morning_end_time', 'afternoon_start_time', 'afternoon_end_time']
