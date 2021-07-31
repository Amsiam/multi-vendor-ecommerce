from django.contrib import admin

# Register your models here.

from .models import ProductCategory, ProductSubCategory


class ProductCategoryAdmin(admin.ModelAdmin):
    exclude = ('parent',)
    list_display = ('title',)
    search_fields = ('title',)


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent',)
    search_fields = ('title', 'parent',)


admin.site.register(ProductSubCategory, ProductSubCategoryAdmin)
