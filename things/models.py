from django.db import models
from django.db.models import Model

class Thing(Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()
