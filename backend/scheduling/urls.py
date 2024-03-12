from . import views
from django.urls import path

urlpatterns = [
    path('scheduling_data/', views.department_list_create_view),
    path('department/<int:pk>/', views.department_detail_view),
    path('department/<int:pk>/update/', views.department_update_view),
    path('department/<int:pk>/delete/', views.department_destroy_view),

    path('instructors/', views.instructor_list_create_view),
    path('instructor/<int:pk>/', views.instructor_detail_view),
    path('instructor/<int:pk>/update/', views.instructor_update_view),
    path('instructor/<int:pk>/delete/', views.instructor_destroy_view),

    path('courses/', views.course_list_create_view),
    path('course/<int:pk>/', views.course_detail_view),
    path('course/<int:pk>/update/', views.course_update_view),
    path('course/<int:pk>/delete/', views.course_destroy_view),
]
