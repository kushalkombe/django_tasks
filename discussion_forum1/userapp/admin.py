from django.contrib import admin
from userapp.models import  User
# Register your models here.

class Useradmin(admin.ModelAdmin):
    list_display=['name','username','password','confirm_password','email','gender','tags']


admin.site.register(User,Useradmin)