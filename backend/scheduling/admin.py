from django.contrib import admin
from .models import ScheduleEntry

class ScheduleEntryAdmin(admin.ModelAdmin):
    list_display = ('parent_schedule', 'course', 'instructor', 'day', 'room', 'start_time', 'end_time')
    search_fields = ('parent_schedule', 'course', 'instructor', 'day', 'room', 'start_time', 'end_time')
    list_filter = ('parent_schedule', 'course', 'instructor', 'day', 'room', 'start_time', 'end_time')

admin.site.register(ScheduleEntry, ScheduleEntryAdmin)