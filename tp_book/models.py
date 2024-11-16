from django.db import models
from datetime import datetime


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    priority = models.IntegerField(default=1)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
