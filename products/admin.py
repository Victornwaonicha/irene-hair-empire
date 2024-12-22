from django.contrib import admin
from .models import Product

# Remove Registration 
#admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at', 'updated_at')  # Columns to display
    list_filter = ('created_at', 'updated_at')  # Add filters
    search_fields = ('name', 'description')  # Search functionality
    ordering = ('-created_at',)  # Newest products first
    list_editable = ('price', 'stock')  # Editable fields in the list view