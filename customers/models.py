from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='customers',)

    def __str__(self):
        return self.name
