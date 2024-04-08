from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import SchedulingData, SchedulingCourse
from .serializers import SchedulingDataSerializer
from .schema import scheduling_data_list_docs

class SchedulingDataAPIView(viewsets.ModelViewSet):
    queryset = SchedulingData.objects.all()
    serializer_class = SchedulingDataSerializer
    
    @scheduling_data_list_docs
    def list(self, request):
        """
        Handle GET request for listing all datas for a specific scheduling data of a department
        at a specific year with optional query parameters.

        This method retrieves a list of department scheduling data based on the provided query parameters
        in the HTTP request.
        Args:
            request (HttpRequest): The HTTP request object containing query parameters.

        Returns:
            Response: A JSON response containing a list of serialized scheduling data objects.

        Raises:
        ValidationError: If the input data is not valid according to the specified criteria.
            - If the JSON data format is invalid.
            - If the duration or frequency for a course is not an integer.
        Query Parameters:
        - 'id' (optional): Filter scheduling data by a specific department ID. Example: 'id=123'.
        - 'year' (optional): Filter scheduling data by a specific year. Example: 'year=2021'.
        - 'batch' (optional): Filter scheduling data by a specific batch. Example: 'batch=3'.

        Example:
        - GET /api/scheduling_config/scheduling_data/
        This will return a list of all the available scheduling data.
        - GET /api/scheduling_config/scheduling_data/?id=123
        This will return details of the department year with ID 123.
        """
        id = request.query_params.get('id')
        year = request.query_params.get('year')
        batch = request.query_params.get('batch')

        if id:
            # Attempt to filter scheduling data by id.
            try:
                self.queryset = self.queryset.filter(id=id)
                if not self.queryset.exists():
                    raise ValidationError(detail=f'Department with id {id} not found')
            except ValueError as exc:
                raise ValidationError(detail='Incorrect department ID format.') from exc
        
        if year:
            # Attempt to filter scheduling data by year.
            try:
                self.queryset = self.queryset.filter(year=year)
                if not self.queryset.exists():
                    raise ValidationError(detail=f'Department data with year {year} not found')
            except ValueError as exc:
                raise ValidationError(detail='Incorrect year format.') from exc
        if batch:            
            # Attempt to filter scheduling data by batch.
            try:
                self.queryset = self.queryset.filter(batch=batch)
                if not self.queryset.exists():
                    raise ValidationError(detail=f'Scheduling data with batch {batch} not found')
            except ValueError as exc:
                raise ValidationError(detail='Incorrect batch format.') from exc
                
        serializer = SchedulingDataSerializer(self.queryset, many=True)
        return Response(serializer.data)
