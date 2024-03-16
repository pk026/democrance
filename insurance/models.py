from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    dob = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class Policy(models.Model):
    POLICY_STATES = [
        ('new', 'New'),
        ('quoted', 'Quoted'),
        ('active', 'Active'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='policies')
    type = models.CharField(max_length=100)
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    cover = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.CharField(max_length=10, choices=POLICY_STATES, default='new')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} - {self.state} - Customer: {self.customer.first_name} {self.customer.last_name}"
