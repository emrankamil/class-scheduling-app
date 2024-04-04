from . import views
from django.urls import path

from rest_framework.routers import DefaultRouter
from .views import DepartmentApiView

router = DefaultRouter()
router.register("departments_data", DepartmentApiView)
router.register("department_year_data", views.DepartmentYearApiView)

urlpatterns = [
] + router.urls
