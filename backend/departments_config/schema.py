from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema

from .serializers import DepartmentSerializer, CourseSerializer, InstructorSerializer

department_list_docs = extend_schema(
    responses=DepartmentSerializer(many=True),
    parameters=[
        OpenApiParameter(
            name='department_id',
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description='Filter departments by a specific department ID.'
        ),
    ]
)