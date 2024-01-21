from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'sku',
        'stock_level',
        'price',
        'rating',
        'image',
        'in_stock',
        'rating',
    )
    # Filter products by category, price, and availability
    list_filter = ('category', 'price', 'in_stock')
    # Sort products by category, subcategory, and brand
    ordering = ('category__name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name',)
    # list_filter = ('subcategory',)
    friendly_name = ('friendly_name',)
    search_fields = ('name', 'friendly_name')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

