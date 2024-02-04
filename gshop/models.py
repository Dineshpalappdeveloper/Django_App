from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=100, blank=True)
    vendoe_id = models.CharField(max_length=100)
