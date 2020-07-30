from django.contrib import admin
from appone.models import *


# Register your models here.
class FaculityAdmin(admin.ModelAdmin):
    list_display=['fname','fnumber','fmail']
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Faculty,FaculityAdmin)
admin.site.register(Batch)
admin.site.register(Studymaterial)
