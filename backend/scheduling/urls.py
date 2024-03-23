from . import views
from django.urls import path

urlpatterns = [
    path('list', views.schedule_list_view),
    path('create', views.schedule_create_view),
    path('<int:pk>/', views.schedule_detail_view),
    path('<int:pk>/update/', views.schedule_update_view),
    path('<int:pk>/delete/', views.schedule_destroy_view),

]
