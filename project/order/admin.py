from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class orderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'email', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['first_name', 'address']
    inlines = [OrderItemInLine]


admin.site.register(Order, orderAdmin)

admin.site.register(OrderItem)