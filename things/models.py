from django.db import models


class Thing(models.Model):
    name = models.CharField()
    description = models.CharField()
    quantity = models.IntegerField()
