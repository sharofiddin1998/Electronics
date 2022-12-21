from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=100)


class Filter_Price(models.Model):
    FILTER_PRICE = (
        ('1000 TO 10000', '1000 TO 10000'),
        ('10000 TO 20000', '10000 TO 20000'),
        ('20000 TO 30000', '20000 TO 30000'),
        ('30000 TO 40000', '30000 TO 40000'),
        ('40000 TO 50000', '40000 TO 50000'),
    )

    price = models.CharField(choices=FILTER_PRICE, max_length=60)

    def __str__(self):
        return self.price


class Product(models.Model):
    CONDITION = (('New', 'New'), ('Old', 'Old'))
    STOCK = (('IN_STOCK', 'IN_STOCK'), ('OUT_OF_STOCK', 'OUT_OF_STOCK'))
    STATUS = (('Publish', 'Publish'), ('Draft', 'Draft'))

    unique_id = models.CharField(unique=True, null=False, max_length=200)
    image = models.ImageField(upload_to='Product_image/img')
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    condition = models.CharField(choices=CONDITION, max_length=100)
    information = RichTextField(null=True)
    description = RichTextField(null=True)
    stock = models.CharField(choices=STOCK, max_length=200)
    status = models.CharField(choices=STATUS, max_length=200)
    create_date = models.DateTimeField(default=timezone.now)    
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_Price, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.unique_id is None and self.create_date and self.id:
            self.unique_id = self.create_date.strftime(
                '75%Y%m%d23') + str(self.id)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Order(models.Model):
    products = models.ManyToManyField(Product, through='OrderProduct')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)


class Images(models.Model):
    image = models.ImageField(upload_to='Product_image/img')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Contact_us(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
