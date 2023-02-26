from django.contrib import admin
from .models import Product, Option

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    pass

# @admin.register(Price)
# class PriceAdmin(admin.ModelAdmin):
#     pass