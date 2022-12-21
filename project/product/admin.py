from django.contrib import admin
from .models import Category

# Register your models here.
@admin.register(Category)
class Product(admin.ModelAdmin):
    list_display = ("name", "slug")