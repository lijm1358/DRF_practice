from django.db import models

# Create your models here.
class Recommend(models.Model):
    User_ID = models.CharField(max_length=30)
    lat = models.FloatField()
    long = models.FloatField()
    epsilon = models.IntegerField()
    keywords = models.CharField(max_length=100)
