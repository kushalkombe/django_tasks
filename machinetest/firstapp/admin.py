from django.contrib import admin
from firstapp.models import Products,Category
# Register your models here.

admin.site.register(Category)
# admin.site.register(Products)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product_name','category','tags','image','description']
    list_filter = ('category', )
    search_fields = ('product_name',)
