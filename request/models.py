from django.db import models

# Create your models here.
class Request(models.Model):
    root = models.TextField()