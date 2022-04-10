from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Order_number)
class Order_numbersAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'data', 'count', 'price', 'date', 'checked_out')
    list_display_links = ('id', 'data')
    readonly_fields = ('count', 'price', 'date')
    search_fields = ('id', 'cart', 'data', 'price', 'date', 'checked_out')
    save_on_top = True


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    # list_display = ('id', 'creation_date', 'checked_out')
    # list_display_links = ('id',)
    # search_fields = ('creation_date', 'checked_out')
    # save_on_top = True
    list_display = ('id', 'user', 'total_count', 'total_price')
    list_display_links = ('id', 'user')
    readonly_fields = ('total_count', 'total_price')
    search_fields = ('id', 'user')
    save_on_top = True


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'quantity', 'unit_price', 'content_type', 'object_id')
    list_display_links = ('id', 'cart')
    readonly_fields = ('cart', 'quantity')
    search_fields = ('cart', 'content_type', 'object_id')
    save_on_top = True
