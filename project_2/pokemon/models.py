from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    description = models.TextField()
    height = models.FloatField()
    order = models.IntegerField()