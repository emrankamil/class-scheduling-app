from . import views
from django.urls import path

urlpatterns = [
    path('departments/', views.department_list_create_view),
    path('departments/<int:pk>/', views.department_detail_view),
    path('departments/<int:pk>/update/', views.department_update_view),
    path('departments/<int:pk>/delete/', views.department_destroy_view),
]
