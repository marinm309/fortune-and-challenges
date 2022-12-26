from django.db import models
from users.models import Customer


class Fortune(models.Model):
    description = models.TextField()


class Challenge(models.Model):
    description = models.TextField()


class UserFortune(models.Model):
    fortune = models.ForeignKey(Fortune, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
