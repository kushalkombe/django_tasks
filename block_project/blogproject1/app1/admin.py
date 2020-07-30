from django.contrib import admin
from.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('id',"title","slug","author","body","publish","created","updated","status")
    prepopulated_fields={"slug":("title",)}
    list_filter=("status","author")
    search_fields =("title","body")
    date_hierarchy=("publish")
    ordering=['status','publish']
admin.site.register(Post,PostAdmin)
