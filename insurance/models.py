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
    PERSONAL_ACCIDENT = "personal-accident"
    HEALTH = "health"
    LIFE = "life"
    TYPE_CHOICES = [
        (PERSONAL_ACCIDENT, 'Personal Accident'),
        (HEALTH, 'Health'),
        (LIFE, 'Life')
    ]
    QUOTED = "quoted"
    ACCEPTED = "accepted"
    BOUND = "bound"
    POLICY_STATES = [
        (QUOTED, 'Quoted'),
        (ACCEPTED, 'Accepted'),
        (BOUND, 'Bound'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='policies')
    type = models.CharField(max_length=32, choices=TYPE_CHOICES)
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    cover = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.CharField(max_length=10, choices=POLICY_STATES, default=QUOTED)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} - {self.state} - Customer: {self.customer.first_name} {self.customer.last_name}"


class PolicyState(models.Model):
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='history')
    state = models.CharField(max_length=10, choices=Policy.POLICY_STATES)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']