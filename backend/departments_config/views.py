# from django.shortcuts import render
# from django.db import transaction
# from rest_framework import generics, status, serializers
# from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import Department, DepartmentYear
from .serializers import DepartmentSerializer, DepartmentYearSerializer


from .schema import department_list_docs

class DepartmentApiView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
    @department_list_docs
    def list(self, request):

        """
        Handle GET request for listing departments with optional query parameters.

        This method retrieves a list of departments based on the provided query parameters
        in the HTTP request.
        Args:
            request (HttpRequest): The HTTP request object containing query parameters.

        Returns:
            Response: A JSON response containing a list of serialized department objects.

        Raises:
            AuthenticationFailed: If the user is not authenticated.
            ValidationError: If there is an issue with the provided query parameters, such 
                as an invalid department ID or incorrect data format.

        Query Parameters:
        - 'department_id' (optional): Filter departments_year data by a specific department ID. Example: 'department_id=123'.
        - 'year' (optional): Filter departments_year data by a specific year.
        - 'batch' (optional): Filter departments_year data by a specific batch.

        Example:
        

        """

        department_id = request.query_params.get('department_id')

        if department_id:
            
            # Attempt to filter departments by department_id.
            try:
                self.queryset = self.queryset.filter(id=department_id)
                if not self.queryset.exists():
                    raise ValidationError(detail=f'Department with id {department_id} not found')
            except ValueError as exc:
                raise ValidationError(detail='Incorrect department ID format.') from exc
        
        serializer = DepartmentSerializer(self.queryset, many=True, )
        return Response(serializer.data)
    
    def create(self, request):
        department_data = request.data
        serializer = DepartmentSerializer(data=department_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class DepartmentYearApiView(viewsets.ModelViewSet):
    queryset = DepartmentYear.objects.all()
    serializer_class = DepartmentYearSerializer
    
    def list(self, request):
        """
        Handle GET request for listing all datas for a specific department at a specific year with optional query parameters.

        This method retrieves a list of department data based on the provided query parameters
        in the HTTP request.
        Args:
            request (HttpRequest): The HTTP request object containing query parameters.

        Returns:
            Response: A JSON response containing a list of serialized department year objects.

        Raises:
        ValidationError: If the input data is not valid according to the specified criteria.
            - If the JSON data format is invalid.
            - If the instructor_id or course_id is not an integer.
            - If the instructor with the given ID does not exist.
            - If the course with the given ID does not exist.
            - If the course_info is not a dictionary.
            - If the course with the given ID does not exist.
            - If the duration or frequency for a course is not an integer.
        Query Parameters:
        - 'department_id' (optional): Filter department years by a specific department ID. Example: 'department_id=123'.

        Example:
        - GET /api/departments_config/department_years/
        This will return a list of all the available department years.
        - GET /api/departments_config/department_years/?department_id=123
        This will return details of the department year with ID 123.

        """
        department_id = request.query_params.get('department_id')
        year = request.query_params.get('year')
        batch = request.query_params.get('batch')

        if department_id:
            
            # Attempt to filter department years by department_id.
            try:
                self.queryset = self.queryset.filter(id=department_id)
                if not self.queryset.exists():
                    raise ValidationError(detail=f'Department with id {department_id} not found')
            except ValueError as exc:
                raise ValidationError(detail='Incorrect department ID format.') from exc
        
        if year:
                
                # Attempt to filter department_years data by year.
                try:
                    self.queryset = self.queryset.filter(year=year)
                    if not self.queryset.exists():
                        raise ValidationError(detail=f'Department data with year {year} not found')
                except ValueError as exc:
                    raise ValidationError(detail='Incorrect year format.') from exc
        
        if batch:
                    
                # Attempt to filter department_years data by batch.
                try:
                    self.queryset = self.queryset.filter(batch=batch)
                    if not self.queryset.exists():
                        raise ValidationError(detail=f'Department data with batch {batch} not found')
                except ValueError as exc:
                    raise ValidationError(detail='Incorrect batch format.') from exc
                
        serializer = DepartmentYearSerializer(self.queryset, many=True)
        return Response(serializer.data)    