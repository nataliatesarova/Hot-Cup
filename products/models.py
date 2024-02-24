from django.db import models
from django.contrib.auth.models import User

"""This is a custom model for Review entity. It will handle the name, the text, and the relation 
to the product by product_id."""
class Review(models.Model):
    review_number = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=512)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', related_name='wishlists')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'created_at']


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254,null=True,blank=True)
    subcategory = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category',null=True,blank=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=254,unique=True)
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True,default=0.00)
    stock_level = models.PositiveIntegerField()
    in_stock = models.BooleanField(default=True)
    rating = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
    
    
    