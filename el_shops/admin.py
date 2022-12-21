from django.contrib import admin
from .models import *
# Register your models here.


class ImagesTublerInline(admin.TabularInline):
    model = Images


class TagTublerInline(admin.TabularInline):
    model = Tag


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesTublerInline, TagTublerInline]


admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact_us)
admin.site.register(Order)
admin.site.register(OrderProduct)
