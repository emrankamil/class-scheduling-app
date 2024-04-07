from django.contrib import admin
from . import models

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', )
    search_fields = ('name', 'id')
    list_filter = ('name', 'id')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'department')
    search_fields = ('name', 'id', 'department')
    list_filter = ('name', 'id', 'department')

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'department')
    search_fields = ('name', 'id', 'department')
    list_filter = ('name', 'id', 'department')

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name', 'id')
    list_filter = ('name', 'id')

admin.site.register(models.Department, DepartmentAdmin)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Instructor, InstructorAdmin)
admin.site.register(models.Room, RoomAdmin)
admin.site.register(models.ReservedRoom)
