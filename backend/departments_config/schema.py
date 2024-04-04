from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema

from .serializers import DepartmentSerializer

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

# department_year_list_docs = extend_schema(
#     responses=DepartmentYearSerializer(many=True),
#     parameters=[
#         OpenApiParameter(
#             name='department_id',
#             type=OpenApiTypes.INT,
#             location=OpenApiParameter.QUERY,
#             description='Filter departments year data by a specific department ID.'
#         ),
#         OpenApiParameter(
#             name='year',
#             type=OpenApiTypes.INT,
#             location=OpenApiParameter.QUERY,
#             description='Filter departments year data by a specific year.'
#         ),
#         OpenApiParameter(
#             name='batch',
#             type=OpenApiTypes.INT,
#             location=OpenApiParameter.QUERY,
#             description='Filter departments year data by a specific batch.'
#         ),
#     ]
# )