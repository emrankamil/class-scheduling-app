from django.contrib import admin
from .models import ScheduleEntry

class ScheduleEntryAdmin(admin.ModelAdmin):
    list_display = ('parent_schedule','day','temp_section', 'course', 'instructor', 'room', 'start_time', 'end_time')
    search_fields = ('parent_schedule','day','temp_section', 'course', 'instructor', 'room', 'start_time', 'end_time')
    list_filter = ('parent_schedule','day','temp_section', 'course', 'instructor', 'room', 'start_time', 'end_time')

admin.site.register(ScheduleEntry, ScheduleEntryAdmin)