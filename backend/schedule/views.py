from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Department
from .models import Course
from .models import Instructor

from .serializers import DepartmentSerializer
from .serializers import CourseSerializer
from .serializers import InstructorSerializer

# department

class ListDataApiView(APIView):

    def get(self, request, format=None, **kwargs):
        departments = Department.objects.all()
        courses = Course.objects.all()
        instructors = Instructor.objects.all()

        department_serializer = DepartmentSerializer(departments, many=True)
        course_serializer = CourseSerializer(courses, many=True)
        instructor_serializer = InstructorSerializer(instructors, many=True)

        return Response({
            'departments': department_serializer.data,
            'courses': course_serializer.data,
            'instructors': instructor_serializer.data
        })

department_list_view = ListDataApiView.as_view()

    # def post(self, request, format=None):
    #     serializer = SnippetSerializer(data=request.data)

    #     department_serializer = DepartmentSerializer(departments)
    #     course_serializer = CourseSerializer(courses)
    #     instructor_serializer = InstructorSerializer(instructors)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DepartmentListCreateApiView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer



class DepartmentDetailApiView(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

department_detail_view = DepartmentDetailApiView.as_view()

class DepartmentUpdateApiView(generics.UpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
      
department_update_view = DepartmentUpdateApiView.as_view()

class DepartmentDestroyApiView(generics.DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

department_destroy_view = DepartmentDestroyApiView.as_view()

#Instructor

class InstructorListCreateApiView(generics.ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

instructor_list_create_view = InstructorListCreateApiView.as_view()

class InstructorDetailApiView(generics.RetrieveAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

instructor_detail_view = InstructorDetailApiView.as_view()

class InstructorUpdateApiView(generics.UpdateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
      
instructor_update_view = InstructorUpdateApiView.as_view()

class InstructorDestroyApiView(generics.DestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

instructor_destroy_view = InstructorDestroyApiView.as_view()

#Course

class CourseListCreateApiView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

course_list_create_view = CourseListCreateApiView.as_view()

class CourseDetailApiView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

course_detail_view = CourseDetailApiView.as_view()

class CourseUpdateApiView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
      
course_update_view = CourseUpdateApiView.as_view()

class CourseDestroyApiView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

course_destroy_view = CourseDestroyApiView.as_view()