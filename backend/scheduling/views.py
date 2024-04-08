
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.forms.models import model_to_dict

from departments_config.models import Course, Instructor, Room
from scheduling_config.models import SchedulingData
from .models import ScheduleEntry
from .serializers import ScheduleEntrySerializer
from scheduling_config.serializers import SchedulingDataSerializer
from .generator import generate_schedule

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
        

        # data = {
        #     'parent_schedule':3,
        #     'course':4,
        #     'instructor':4,
        #     'day':'MONDAY',
        #     'room':4,
        #     'start_time':'08:00:00',
        #     'end_time':'09:00:00',
        # }

        scheduling_id = request.query_params.get('scheduling_id')
        
        generate_schedule(4, ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY'])
        # new_entry = ScheduleEntrySerializer(data=data)
        # if new_entry.is_valid():
        #     new_entry.save()
        # else:
        #     print(new_entry.errors)
        #     raise ValidationError(new_entry.errors)

        serializer = ScheduleEntrySerializer(self.queryset, many=True, )
        return Response(serializer.data)
    

    
