from django.db import models

# Create your models here.
class Subway(models.Model):
    starting = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)