from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Department)
admin.site.register(models.Course)
admin.site.register(models.Instructor)
admin.site.register(models.Room)
admin.site.register(models.DepartmentYear)
