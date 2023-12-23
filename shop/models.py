from django.db import models

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

