from django.db import models
import datetime
from pytz import timezone

# Create your models here.
class Checkin(models.Model):
    User_ID = models.CharField(max_length=30)
    lat = models.FloatField()  #-85~85
    long = models.FloatField() #-180~180
    timeStamp = models.DateTimeField(auto_now_add=True)
