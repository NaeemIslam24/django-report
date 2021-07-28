from django.db import models
from products.models import Product
from customers.models import Customer
from profiles.models import Profile
from django.utils import timezone
from . utils import genarae_code


class Position(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)
    created = models.DateTimeField(blank=True)

    def __str__(self):
        return f"id: {self.id} product: {self.product.name} quantity: {self.quantity}"

    def save(self, *args, **kwargs):

        self.price = self.product.price * self.quantity

        return super().save(*args, **kwargs)


class Sale(models.Model):
    transaction_id = models.CharField(max_length=20, blank=True)
    position = models.ManyToManyField(Position)
    totol_price = models.FloatField(blank=True, null=True)
    customers = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesman = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    updarted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"In $ {self.totol_price}"

    def save(self, *args, **kwargs):

        if self.transaction_id == "":
            self.transaction_id = genarae_code()
        if self.created is None:
            self.created = timezone.now()

        return super().save(*args, **kwargs)


class CSV(models.Model):

    file_name = models.FileField(upload_to='csvs')
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file_name)
