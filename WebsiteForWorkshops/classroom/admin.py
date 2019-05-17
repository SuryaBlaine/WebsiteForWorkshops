from django.contrib import admin
from .models import classroom,classroomjoin,classroomteach

# Register your models here.
admin.site.register(classroom)
admin.site.register(classroomjoin)
admin.site.register(classroomteach)

