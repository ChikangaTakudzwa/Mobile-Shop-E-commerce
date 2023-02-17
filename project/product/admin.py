from django.contrib import admin
from .models import Category, Product, Review

# Register your models here.
@admin.register(Category)
class ProductCategory(admin.ModelAdmin):
    list_display = ("name", "slug")

@admin.register(Product)
class Products(admin.ModelAdmin):
    list_display = ("category", "name", "model", "slug", "description", "price", "created_at")

@admin.register(Review)
class Products(admin.ModelAdmin):
    list_display = ("id", "product", "rating", "content", "created_by", "content")
