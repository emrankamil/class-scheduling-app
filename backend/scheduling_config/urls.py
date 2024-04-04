from . import views
from django.urls import path

from rest_framework.routers import DefaultRouter
from .views import SchedulingDataAPIView

router = DefaultRouter()
router.register("scheduling_data", SchedulingDataAPIView)
# router.register("department_year_data", views.DepartmentYearApiView)

urlpatterns = [
] + router.urls
