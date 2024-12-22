from django.db import models

class Product(models.Model):
    """
    Represents a product for sale in Irene Hair Empire.
    """

    name = models.CharField(max_length=255)  # The product's name
    description = models.TextField(blank=True)  # A brief description of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product
    stock = models.PositiveIntegerField(default=0)  # Number of items available in stock
    image = models.ImageField(upload_to='product_images/')  # Product image
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the product was added
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for when the product was last updated
    is_active = models.BooleanField(default=True)  # Indicates if the product is available for sale

    def __str__(self):
        """
        Returns a string representation of the product.
        """
        return self.name

# Create your models here.
