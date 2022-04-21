from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=300)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.user

class Item(models.Model):
    STATUS = [
        ('In progress', 'In progress'),
        ('Completed', 'Completed'),
    ]

    customer= models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    item = models.CharField(max_length=500)
    status = models.CharField(max_length=100, choices=STATUS, default='In progress')

    def __str__(self):
        return self.item

