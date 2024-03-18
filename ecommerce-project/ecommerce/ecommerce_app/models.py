from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='products_images', blank=True)
    product_discount_price = models.FloatField()
    product_original_price = models.FloatField()
    product_quantity = models.IntegerField(null=True, blank=True)
    digital = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.product_name
    
    @property
    def imageURL(self):
        try:
            url = self.product_image.url
        except:
            url = ''
        return url
    
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateField(auto_now_add=True)
    shipped=models.BooleanField(default=False)
    transaction_id=models.IntegerField(null=True)

    def __str__(self):
        return str(self.transaction_id)
    
    @property
    def get_cart_item(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    

class OrderItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(null=True, default=0, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.product_discount_price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address