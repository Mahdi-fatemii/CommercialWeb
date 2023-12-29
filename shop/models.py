from django.db import models
from user.models import User
# Create your models here.


class Product(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=1000, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGzq7-nyJRg83b4i_CjXMi9mYUE1wx1XVTxBGp-cLvE-apW9KzaYi2wkVDt_G-v49mF2E&usqp=CAU")


class Cart(models.Model):

    def __int__(self):
        return self.cart_status

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    cart_status = models.CharField(max_length=100, default='Pending')


class CartItems(models.Model):

    def __int__(self):
        return self.cart_id

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Payment(models.Model):

    def __int__(self):
        return self.cart_id

    cart_id = models.OneToOneField(Cart, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=100, default='Pending')
    price = models.FloatField()







