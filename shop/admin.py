from unicodedata import category
from django.contrib import admin
from .models import Products, Orders
# Register your models here.

admin.site.site_header = "E-commerce Site"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Manage ABC Shopping"


class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, queryset):
        queryset.update(category= 'default')
    
    list_display = ('title', 'price', 'discounted_price', 'category')
    search_fields = ('title',)
    actions = ('change_category_to_default',)
    change_category_to_default.short_description = 'Default Category'
    fields = ()
    list_editable = ('price', 'category')


admin.site.register(Products, ProductAdmin)
admin.site.register(Orders)