from django.db import models

class Fortune(models.Model):
    description = models.TextField()


class Challenge(models.Model):
    description = models.TextField()
