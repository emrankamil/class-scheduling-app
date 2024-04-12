from django.contrib import admin
from . import models

class SchedulingDataAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', )
    search_fields = ('__str__', 'id')

class SchedulingCourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'id', 'scheduling_data')
    search_fields = ('course', 'id', 'scheduling_data')
    list_filter = ('course', 'id', 'scheduling_data')

admin.site.register(models.SchedulingData, SchedulingDataAdmin)
admin.site.register(models.SchedulingCourse, SchedulingCourseAdmin)
admin.site.register(models.Section)