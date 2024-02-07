from django.db import models

# Create your models here.


class ShowRoomsList(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    website = models.URLField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'showroomslist'


class CarList(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    chassisnumber = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    ShowRoomsList = models.ForeignKey(
        ShowRoomsList, on_delete=models.CASCADE, null=True, related_name='showRoomsList')

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=100, blank=True)
    userIDs = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    fee = models.IntegerField()


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    price = models.IntegerField()


class VendorOne(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=100, blank=True)
    vendoe_id = models.CharField(max_length=100)

# models.py in gsop_app


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        # Specify the desired table name without the app prefix
        db_table = 'product'
