from django.contrib import admin

from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category')
    list_filter = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('category_name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
