from django.db import models
from user.models import CustomUser
from django.utils import timezone
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

    class Meta:
        ordering = ['-id']


class Cart(models.Model):

    def __str__(self):
        return self.user.email

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cart_status = models.CharField(max_length=100, default='Pending')
    total_price = models.FloatField()


class CartItem(models.Model):

    def __str__(self):
        return self.cart_id.user.email

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Payment(models.Model):

    def __str__(self):
        return self.cart_id.user.email

    cart_id = models.OneToOneField(Cart, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=100, default='Pending')
    price = models.FloatField()
    status = models.CharField(max_length=50, default="pending")
    token = models.CharField(max_length=500, default=0)
    refid = models.CharField(max_length=500, default=0)
    card_pan = models.CharField(max_length=500, default=0)
    transaction_id = models.CharField(max_length=500, default=0)
    date_created = models.DateTimeField(default=timezone.now)


class PaymentInfo(models.Model):

    def __str__(self):
        return self.mobile_number

    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=500, null=True)
    mobile_number = models.CharField(max_length=11)
    email = models.EmailField("email address", blank=True, null=True)
    discount = models.CharField(max_length=100, blank=True, null=True, default=00000)



