from django.contrib import admin
from .models import ExtraImages, Product
from product.models import DiscountType
from datetime import datetime
# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ExtraImages
    max_num = 5


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

    list_display = ["title", "price", "discount_price", "category",
                    "in_stock",  "status"]

    fieldsets = (
        (None, {
            "fields": ("title", "price", "category", "thumbnail", "description", "in_stock", "status"),
        }),
        ("Discount", {
            "fields": ("discount_type", "discount", "discount_start", "discount_end"),
        })
    )

    def save_model(self, request, obj, form, change):

        if(not change):
            obj.added_by = request.user
        return super().save_model(request, obj, form, change)

    def discount_price(self, obj):
        if(obj.discount_type == DiscountType.none):
            return "No Discount Running on"
        else:
            timenow = datetime.now()
            if(obj.discount_start <= timenow and timenow <= obj.discount_end):
                if(obj.discount_type == DiscountType.money):
                    return obj.price - obj.discount
                else:
                    return obj.price - (obj.discount*0.01*obj.price)
            else:
                return "No Discount Running on"

    readonly_fields = ('slug',)


admin.site.register(Product, ProductAdmin)
