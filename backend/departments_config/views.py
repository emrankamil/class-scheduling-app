from django.shortcuts import render
from django.db import transaction
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

    def post(self, request, format=None):

        try:
            with transaction.Atomic(using=None, savepoint=True, durable=True):
                
                course_data = request.data.get('courses', [])
                instructor_data = request.data.get('instructors', [])
                department_data = request.data.get('department', [])

                course_serializer = CourseSerializer(data=course_data, many=True)
                instructor_serializer = InstructorSerializer(data = instructor_data, many=True)

                if course_serializer.is_valid() and instructor_serializer.is_valid():
                    course_serializer.save()
                    course_ids = [course['id'] for course in course_serializer.data]

                    instructor_serializer.save()
                    instructor_ids = [instructor['id'] for instructor in instructor_serializer.data]
                    
                    department_data['courses'] = course_ids
                    department_data['instructors'] = instructor_ids
                    department_serializer = DepartmentSerializer(data=department_data)

                    if department_serializer.is_valid():
                        department_serializer.save()
                        return Response({'message': 'Data saved successfully.'}, status=status.HTTP_201_CREATED)
                    else:
                        return Response({'error': 'Validation failed.', 'department_errors': department_serializer.errors},
                                        status=status.HTTP_400_BAD_REQUEST)
                    
                else:
                    return Response({
                        'error': 'Validation failed.',
                        'department_errors': department_serializer.errors,
                        'course_errors': course_serializer.errors,
                        'instructor_errors': instructor_serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
department_list_create_view = ListDataApiView.as_view()

# class DepartmentListCreateApiView(generics.ListCreateAPIView):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer


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



# {
# "department": 
#     {
#         "name": "New Department",
#         "courses": [],
#         "instructors": [],
#         "assigned_days": ["monday", "tuesday"],
#         "rooms": ["12", "22"]
#     }
# ,
# "instructors": [
#     {
#         "name": "Emran"
#     },
#     {
#         "name": "Bereket Werku"
#     },
#     {
#         "name": "Ayenew Alayenew"
#     }
# ],
# "courses": [
#     {
#         "name": "Fundamentls Of Electronics",
#         "credit_hour": "10"
#     },
#     {
#         "name": "Circuit Design",
#         "credit_hour": "7"
#     },
#     {
#         "name": "Introduction to Python Programming",
#         "credit_hour": "3"
#     }
# ]
# }