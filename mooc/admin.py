from django.contrib import admin
from mooc.models import Course, CourseAdmin

# Register your models here.
admin.site.register(Course, CourseAdmin)
