from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema

from .serializers import SchedulingDataSerializer

scheduling_data_list_docs = extend_schema(
    responses=SchedulingDataSerializer(many=True),
    parameters=[
        OpenApiParameter(
            name='department_id',
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description='Filter scheduling data by a specific department ID.'
        ),
        OpenApiParameter(
            name='year',
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description='Filter scheduling data by a specific year.'
        ),
        OpenApiParameter(
            name='batch',
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description='Filter scheduling data by a specific batch.'
        ),
    ]
)