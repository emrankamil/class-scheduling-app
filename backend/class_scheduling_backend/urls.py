from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/departments_config/', include('departments_config.urls')),
    path('api/scheduling_config/', include('scheduling_config.urls')),
    path('api/schedule/', include('scheduling.urls')),
    path('api/docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/schema/ui/', SpectacularSwaggerView.as_view(), name='swagger-ui'),
]
