# from django.shortcuts import render
# from django.db import transaction
# from rest_framework import generics, status, serializers
# from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import Department
from .serializers import DepartmentSerializer


from .schema import department_list_docs

class DepartmentListView(viewsets.ModelViewSet):
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
        - 'department_id' (optional): Filter departments by a specific department ID. Example: 'department_id=123'.

        Example:
        - GET /api/departments_config/departments_data/
        This will return a list of all the available departments.
        - GET /api/departments_config/departments_data/?department_id=123
        This will return details of the department with ID 123.

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