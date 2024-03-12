from django.shortcuts import render
from rest_framework import generics

from .models import Schedule
from .serializers import ScheduleSerializer

class ScheduleListCreateApiView(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

schedule_list_create_view = ScheduleListCreateApiView.as_view()

class ScheduleDetailApiView(generics.RetrieveAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

schedule_detail_view = ScheduleDetailApiView.as_view()

class ScheduleUpdateApiView(generics.UpdateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
      
schedule_update_view = ScheduleUpdateApiView.as_view()

class ScheduleDestroyApiView(generics.DestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

schedule_destroy_view = ScheduleDestroyApiView.as_view()
