from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()
route.register('', views.ScheduleApiView, basename='schedule')
urlpatterns = [
] + route.urls
