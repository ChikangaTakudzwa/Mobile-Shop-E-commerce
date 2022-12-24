from django.contrib import admin
from .models import Category, Product

# Register your models here.
@admin.register(Category)
class ProductCategory(admin.ModelAdmin):
    list_display = ("name", "slug")

# Register your models here.
@admin.register(Product)
class Products(admin.ModelAdmin):
    list_display = ("category", "name", "model", "slug", "description", "price", "created_at")