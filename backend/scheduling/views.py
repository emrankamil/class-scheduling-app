from django.shortcuts import render
from rest_framework import generics
from .models import Department
from .serializers import SchedulingSerializer

class DepartmentListCreateApiView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = SchedulingSerializer

department_list_create_view = DepartmentListCreateApiView.as_view()

class DepartmentDetailApiView(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = SchedulingSerializer

department_detail_view = DepartmentDetailApiView.as_view()

class DepartmentUpdateApiView(generics.UpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = SchedulingSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
      
department_update_view = DepartmentUpdateApiView.as_view()

class DepartmentDestroyApiView(generics.DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = SchedulingSerializer

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

department_destroy_view = DepartmentDestroyApiView.as_view()