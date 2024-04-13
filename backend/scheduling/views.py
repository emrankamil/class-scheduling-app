
from rest_framework import viewsets
from rest_framework.response import Response
from .models import ScheduleEntry
from .serializers import ScheduleEntrySerializer
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
        scheduling_id = request.query_params.get('scheduling_id')
        if scheduling_id:
            generate_schedule(scheduling_id, ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY'])
            self.queryset = ScheduleEntry.objects.filter(parent_schedule=scheduling_id)

        serializer = ScheduleEntrySerializer(self.queryset, many=True, )
        return Response(serializer.data)
    

    
