from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import ScheduleEntry
from departments_config.models import Department, Course, Instructor, Room
from scheduling_config.models import SchedulingData, SchedulingCourse
from .serializers import ScheduleEntrySerializer


class ScheduleApiView(viewsets.ModelViewSet):
    queryset = ScheduleEntry.objects.all()
    serializer_class = ScheduleEntrySerializer

    
    def list(self, request):

        """
        Handle GET request for ... 

        Args:
            request (HttpRequest): The HTTP request object containing query parameters.

        Returns:
            Response: A JSON response containing a list of serialized department objects.

        Raises:
            AuthenticationFailed:
            ValidationError: 

        Query Parameters:
        Example:
        
        """
        scheduling_id = request.query_params.get('scheduling_id')
        course = Course.objects.get(id=1)
        instructor = Instructor.objects.get(id=1)
        room = Room.objects.get(id=1)
        parent_schedule = SchedulingData.objects.get(id=scheduling_id)

        data = {
            'parent_schedule':3,
            'course':4,
            'instructor':4,
            'day':'MONDAY',
            'room':4,
            'start_time':'08:00:00',
            'end_time':'09:00:00',
        }
        
        new_entry = ScheduleEntrySerializer(data=data)
        if new_entry.is_valid():
            new_entry.save()
        else:
            print(new_entry.errors)
            raise ValidationError(new_entry.errors)

        serializer = ScheduleEntrySerializer(self.queryset, many=True, )
        return Response(serializer.data)
    

    

# class ScheduleListApiView(generics.ListAPIView):
#     queryset = ScheduleEntry.objects.all()
#     serializer_class = ScheduleEntrySerializer

# schedule_list_view = ScheduleListApiView.as_view()

# class ScheduleCreateApiView(generics.CreateAPIView):
#     queryset = ScheduleEntry.objects.all()
#     serializer_class = ScheduleEntrySerializer

# schedule_create_view = ScheduleCreateApiView.as_view()

# class ScheduleDetailApiView(generics.RetrieveAPIView):
#     queryset = ScheduleEntry.objects.all()
#     serializer_class = ScheduleEntrySerializer

# schedule_detail_view = ScheduleDetailApiView.as_view()

# class ScheduleUpdateApiView(generics.UpdateAPIView):
#     queryset = ScheduleEntry.objects.all()
#     serializer_class = ScheduleEntrySerializer
#     lookup_field = 'pk'

#     def perform_update(self, serializer):
#         instance = serializer.save()
      
# schedule_update_view = ScheduleUpdateApiView.as_view()

# class ScheduleDestroyApiView(generics.DestroyAPIView):
#     queryset = ScheduleEntry.objects.all()
#     serializer_class = ScheduleEntrySerializer

#     def perform_destroy(self, instance):
#         super().perform_destroy(instance)

# schedule_destroy_view = ScheduleDestroyApiView.as_view()
