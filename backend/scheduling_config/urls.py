from django.urls import path

from rest_framework.routers import DefaultRouter
from .views import SchedulingDataAPIView, SchedulingCourseAPIView, SectionAPIView

router = DefaultRouter()
router.register("scheduling_data", SchedulingDataAPIView)
router.register("scheduling_courses", SchedulingCourseAPIView)
router.register("section", SectionAPIView)

urlpatterns = [
] + router.urls
